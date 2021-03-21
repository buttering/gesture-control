import os

import cv2
import mediapipe as mp
import numpy as np
import time

'''
    用于手势关键点数据的录制
'''
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
input_points = [0, 2, 4, 5, 8, 9, 12, 13, 16, 17, 20]
# hand1 = np.zeros(528,dtype='float32')
# hand2 = np.zeros(528,dtype='float32')
# (16,33)
hand1_frames = []
hand2_frames = []
# TODO： 数据存储路径，两只手的数据分别存在root_dir/label/hand1/ 与root_dir/label/hand2目录下,当录制单手数据集时，hand2目录下的数据为全0。所以删除无效数据时记得删除两个文件。
root_dir = 'C:/Users/Administrator/Desktop/testset'
# TODO: 数据类别,标签从0开始计数，3表示第3类手势（"Swiping Right"），每一类手势具体指代详见当前目录下our_label_map.txt。10、11、12应该是合理的数据
label = '0'
n = 0
# For webcam input:
# 实时检测手势
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=0.80,
        min_tracking_confidence=0.25) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = hands.process(image)
        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        y = mp_hands.HandLandmark
        if results.multi_hand_landmarks:
            n += 1
            if n%3 == 0:
                # x = results.multi_hand_landmarks
                # print(len(x))
                # (2,16,11*3,)
                hand1 = []
                hand2 = []
                hand_idx = 0
                for hand_landmarks in results.multi_hand_landmarks:
                    hand_idx += 1
                    if hand_idx == 1:
                        for idx in input_points:
                            hand1.append(round(hand_landmarks.landmark[idx].x,3))
                            hand1.append(round(hand_landmarks.landmark[idx].y,3))
                            hand1.append(round(hand_landmarks.landmark[idx].z,3))
                    else:
                        for idx in input_points:
                            hand2.append(round(hand_landmarks.landmark[idx].x,3))
                            hand2.append(round(hand_landmarks.landmark[idx].y,3))
                            hand2.append(round(hand_landmarks.landmark[idx].z,3))
                    # 打印出手腕的x,y,z坐标，屏幕左上角是坐标原点，右下角是（1,1，z）
                    # print(hand_landmarks.landmark[0].x, hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y,
                    #       hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z)
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                if len(results.multi_hand_landmarks) == 1:
                    # 只有一只手时，另一只手的坐标全用0替代
                    for idx in input_points:
                        for i in range(3):
                            hand2.append(.0)
                hand1_frames.append(hand1)
                hand2_frames.append(hand2)
                if n == 48:
                    # TODO
                    save_dir_1 = os.path.join(root_dir,label,'hand1')
                    save_dir_2 = os.path.join(root_dir,label,'hand2')
                    if not os.path.exists(save_dir_1):
                        os.mkdir(save_dir_1)
                        os.mkdir(save_dir_2)
                    file_name = '{}.txt'.format(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
                    np.savetxt(os.path.join(save_dir_1,file_name),hand1_frames)
                    np.savetxt(os.path.join(save_dir_2,file_name),hand2_frames)
                    print(np.loadtxt(os.path.join(save_dir_1,file_name)))
                    # with open(os.path.join(root_dir,'3','hand1.txt'),'a') as f:
                    #     f.writelines(str(hand1_frames).replace('[','').replace(']','').replace(',',''))
                    # with open(os.path.join(root_dir,'3','hand2.txt'),'a') as f:
                    #     f.writelines(str(hand2_frames).replace('[','').replace(']','').replace(',',''))
                    hand1_frames = []
                    hand2_frames = []
                    n = 0
                    time.sleep(2)
                    # break

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()

def get_0():
    pass