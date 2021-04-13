import numpy as np
import time
import cv2
import torch
import torch.onnx
from PIL import Image, ImageOps

# 在引入父目录的模块之前加上如下代码：
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))

from client import socketClient
from config import socketConfig
from model.dnn import DNN
import mediapipe as mp

SOFTMAX_THRES = 0.99  # 输出手势的阈值
HISTORY_LOGIT = True
REFINE_OUTPUT = True


'''
    现在的缺点，刚伸出手时容易误识别为swip right(已解决)，刚伸出双手容易误识别为zoom in（仍有小概率）
'''
model_path = 'model/2021-03-19-14-34-56_acc90.pkl'  # best
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
input_points = [0, 2, 4, 5, 8, 9, 12, 13, 16, 17, 20]
# hand1_buf = torch.zeros(528)
# hand2_buf = torch.zeros(528)
# 16帧，11个点，每个点xyz3个坐标
hand1_buf = torch.rand(16 * 11 * 3)
hand2_buf = torch.rand(16 * 11 * 3)
two_hand = [7, 8, 9, 10, 11]
one_hand = [1, 3, 4, 5, 6, 12, 13]
catigories = [
    "Doing other things",
    "Click",
    "No gesture",
    "Swiping Right",
    "Swiping Left",
    "Swiping Up",
    "Grab",
    "Zooming In",
    "Zooming Out",
    "Turning Clockwise",
    "Turning Counterclockwise",
    "Thumb Up",
    "Thumb Down",
]

n_still_frame = 0


def process_input(hand1, hand2):
    # 将双手数据拼接在一起作为输入
    global hand1_buf, hand2_buf
    hand1_buf = torch.cat((hand1_buf, hand1))
    hand2_buf = torch.cat((hand2_buf, hand2))
    hand1_buf = hand1_buf[33:]
    hand2_buf = hand2_buf[33:]
    input_data = torch.cat((hand1_buf, hand2_buf))
    return input_data


def process_output(idx_, history):
    # idx_: the output of current frame
    # history: a list containing the history of predictions
    if not REFINE_OUTPUT:
        return idx_, history

    max_hist_len = 20  # max history buffer

    # 减少双手动作对单手动作的误识别情况，主要是减少将伸出双手误识别为swip right的情况
    if idx_ in one_hand and (torch.sum(hand2_buf != 0)) > 33:
        idx_ = history[-1]

    # 减少单手动作对双手动作的误识别
    if idx_ in two_hand and (torch.sum(hand2_buf != 0)) < 400:  # + torch.sum(hand2_buf!=0)) < 600:
        idx_ = history[-1]

    # use only single no action class
    if idx_ == 0:
        idx_ = 2

    history.append(idx_)

    # thres为3可以避免伸出双手的误识别的情况
    thres = 3  # 取为3时必须连续3次出现同一类别才允许输出值越高误识别率应该可以降低但准确率可能会受到影响
    # history smoothing
    if idx_ != history[-1]:
        idx_ = history[-1]
    for i in range(1, thres):
        if history[-i] != history[-i - 1]:
            history = history[-max_hist_len:]
            return history[-thres - 1], history
            # break
        # if history[-1] != history[-2] and history[-2] != history[-3]:
        #     idx_ = history[-1]

    history = history[-max_hist_len:]

    # return history[-1], history
    return idx_, history


def clear_buf():
    # 清空手部数据缓存区
    global hand2_buf, hand1_buf
    # 全部清空为0
    hand2_buf[:] = 0
    hand1_buf[:] = 0
    # 全部清空为1
    # hand1_buf = torch.ones(528)
    # hand2_buf = torch.ones(528)
    # 以随机数的方式清空
    # hand1_buf = torch.rand(528)
    # hand2_buf = torch.rand(528)


WINDOW_NAME = 'Video Gesture Recognition'


class GestureRecognize:
    # 保存客户端实例
    FLAG = 0  # 默认不开启手势识别
    time_thre = 2
    __client = None
    __last = time.time()
    __gesture_list = ["Doing other things", "click", "No gesture",
                      "panRight", "panLeft", "focus",
                      "grasp", "enlarge", "narrow",
                      "cwr", "ccwr", "like", "unlike"]

    def socket_out(self, output):
        if output == 2:
            self.__client.focus_interface_field()
        if output == 5:
            self.FLAG = not self.FLAG
            print(self.FLAG)
        elif output not in [0, 2] and self.FLAG:
            # 为有效手势
            cur = time.time()
            seg = cur - self.__last
            if seg > self.time_thre:
                print(seg)
                # socket发送消息
                self.__client.gestureFilter(self.__gesture_list[output])
                self.__last = cur

    # 启动socket客户端，与socket服务器进行连接
    def startUpClient(self, ip: str = '127.0.0.1', port: int = 9000) -> bool:
        # 与服务器进行连接
        attempt = 5  # 网络连接尝试次数
        inteval = 1  # 重连间隔
        print("连接服务器中")
        self.__client = socketClient.SocketClient()
        for i in range(attempt):
            if self.__client.startUp(ip, port):
                break
            else:
                print(f"服务器连接失败……{inteval}秒后重试……剩余{attempt - i}次")
                time.sleep(inteval)
            if i == attempt - 1:
                print("服务器连接失败，请检查后重新启动")
                return False
        print("连接成功！")
        return True

    def main(self, show_windows=True):
        print("Open camera...")
        cap = cv2.VideoCapture(0)

        # set a lower resolution for speed up
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

        # env variables
        full_screen = False
        if show_windows:
            cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(WINDOW_NAME, 640, 480)
            cv2.moveWindow(WINDOW_NAME, 0, 0)
            cv2.setWindowTitle(WINDOW_NAME, WINDOW_NAME)

        t = None
        index = 0
        model = DNN()
        model.load_state_dict(torch.load(model_path))
        model.eval()

        idx = 0
        history = [2, 2] * 5
        history_logit = []
        history_timing = []

        i_frame = -1

        print("Ready!")
        with mp_hands.Hands(
                min_detection_confidence=0.80,
                min_tracking_confidence=0.25) as hands:
            with torch.no_grad():
                while cap.isOpened():
                    t1 = time.time()
                    i_frame += 1
                    success, image = cap.read()  # (480, 640, 3) 0 ~ 255
                    # Flip the image horizontally for a later selfie-view display, and convert
                    # the BGR image to RGB.
                    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                    # if i_frame%3 == 0:  # skip every other frame to obtain a suitable frame rate
                    # To improve performance, optionally mark the image as not writeable to
                    # pass by reference.
                    image.flags.writeable = False
                    results = hands.process(image)
                    # Draw the hand annotations on the image.
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    # TODO 2或3选一个
                    # if i_frame % 2 == 0:  # skip every other frame to obtain a suitable frame rate
                    if True:
                        if results.multi_hand_landmarks:
                            hand1 = []
                            hand2 = []
                            hand_idx = 0
                            # print("hand:{}".format(len(results.multi_hand_landmarks)))
                            for hand_landmarks in results.multi_hand_landmarks:
                                hand_idx += 1
                                if hand_idx == 1:
                                    for i in input_points:
                                        hand1.append(round(hand_landmarks.landmark[i].x, 3))
                                        hand1.append(round(hand_landmarks.landmark[i].y, 3))
                                        hand1.append(round(hand_landmarks.landmark[i].z, 3))
                                else:
                                    for i in input_points:
                                        hand2.append(round(hand_landmarks.landmark[i].x, 3))
                                        hand2.append(round(hand_landmarks.landmark[i].y, 3))
                                        hand2.append(round(hand_landmarks.landmark[i].z, 3))
                                # 打印出手腕的x,y,z坐标，屏幕左上角是坐标原点，右下角是（1,1，z）
                                # print(hand_landmarks.landmark[0].x, hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y,
                                #       hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z)
                                mp_drawing.draw_landmarks(
                                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                            if len(results.multi_hand_landmarks) == 1:
                                # 只检测到一只手时，另一只手的坐标全用0替代
                                for j in input_points:
                                    for i in range(3):
                                        hand2.append(.0)
                            # try:
                            # 将左右手的坐标拼接为模型的输入
                            input_var = process_input(torch.tensor(hand1), torch.tensor(hand2))
                            # except RuntimeError:

                            # 如果输入的数组非0的个数小于400数组大小为3*11*2*16=1056，则
                            if torch.sum(input_var != 0) < 400:
                                out_put = torch.zeros((1, 13))
                                out_put[0, 2] = 1
                            else:
                                input_var = input_var[:1056]  # 防止出现shape不匹配的问题
                                out_put = model(input_var.reshape(1, -1))
                            # print(len(hand1_buf), input_var.shape)
                        else:
                            # 若没检测到手则清空缓存帧，防止对下次识别造成影响
                            # global hand1_buf, hand2_buf
                            clear_buf()
                            out_put = torch.zeros((1, 13))
                            out_put[0, 2] = 1
                        # 阈值
                        if SOFTMAX_THRES > 0:
                            feat_np = out_put.numpy().reshape(-1)
                            feat_np -= feat_np.max()
                            softmax = np.exp(feat_np) / np.sum(np.exp(feat_np))

                            # print(softmax)
                            if max(softmax) > SOFTMAX_THRES:
                                idx_ = np.argmax(out_put.numpy(), axis=1)[0]
                            else:
                                # idx_ = idx
                                idx_ = 2
                        else:
                            idx_ = np.argmax(out_put.cpu().numpy(), axis=1)[0]

                        idx, history = process_output(idx_, history)

                        # 调用socket函数
                        self.socket_out(idx)
                        # print(idx,out_put)
                        # print(f"{index} {catigories[idx]}")
                    if show_windows:
                        t2 = time.time()
                        current_time = t2 - t1
                        image = cv2.resize(image, (640, 480))
                        # image = image[:, ::-1]
                        height, width, _ = image.shape
                        label = np.zeros([height // 10, width, 3]).astype('uint8') + 255

                        cv2.putText(label, 'Prediction: ' + catigories[idx],
                                    (0, int(height / 16)),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.7, (0, 0, 0), 2)
                        if current_time==0 :
                            current_time = 1
                        cv2.putText(label, '{:.1f} Vid/s'.format(1 / current_time),
                                    (width - 170, int(height / 16)),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.7, (0, 0, 0), 2)
                        #
                        image = np.concatenate((image, label), axis=0)
                        cv2.imshow(WINDOW_NAME, image)  # TODO

                    # key = cv2.waitKey(1)
                    if cv2.waitKey(5) & 0xFF == 27:  # exit
                        break

                    if t is None:
                        t = time.time()
                    else:
                        nt = time.time()
                        index += 1
                        t = nt

                cap.release()
                cv2.destroyAllWindows()


if __name__ == '__main__':
    gestureRecognize = GestureRecognize()
    # if gestureRecognize.startUpClient(socketConfig.IP, socketConfig.PORT):
    if gestureRecognize.startUpClient():
        gestureRecognize.main()
