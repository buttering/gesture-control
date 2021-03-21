# coding=utf-8
import os
import cv2
import numpy as np

# videos_src_path = "C:\\Users\\86135\\Desktop\\学习\\服创数据\\try\\"
videos_src_path = 'D:/CSU/data3/customize_ges/所有数据/抓取/'
# video_formats = [".MP4", ".MOV"]
# frames_save_path = "C:\\Users\\86135\\Desktop\\reasult\\"
frames_save_path = 'D:/CSU/data3/customize_ges/frames/6/'
width = 176
height = 100
time_interval = 10
alpha = [1.2, 0.8]
beta = [20, -20]


def Contrast_and_Brightness(alpha, beta, img):
    # reference: https://blog.csdn.net/qq_33840601/article/details/90400375
    blank = np.zeros(img.shape, img.dtype)
    # dst = alpha * img + (1-alpha) * blank + beta
    dst = cv2.addWeighted(img, alpha, blank, 1 - alpha, beta)
    return dst


def video2frame(video_src_path, frame_save_path, frame_width, frame_height, interval):
    """
    将视频按固定间隔读取写入图片
    :param video_src_path: 视频存放路径
    :param formats:　包含的所有视频格式
    :param frame_save_path:　保存路径
    :param frame_width:　保存帧宽
    :param frame_height:　保存帧高
    :param interval:　保存帧间隔
    :return:　帧图片
    """
    m = 152217
    videos = os.listdir(video_src_path)
    for each_video in videos:
        print("正在读取视频：", each_video)
        each_video_name = str(m)
        m = m + 1
        os.mkdir(frame_save_path + each_video_name)
        for i in range(1, 5):
            os.mkdir(frame_save_path + each_video_name + '_{}'.format(i))
        each_video_save_full_path = os.path.join(frame_save_path, each_video_name)

        each_video_full_path = os.path.join(video_src_path, each_video)

        cap = cv2.VideoCapture(each_video_full_path)
        FPS = cap.get(5) * 0.0833333
        frame_index = 0
        frame_count = 1
        n = 1
        if cap.isOpened():
            success = True
        else:
            success = False
            print("读取失败!")
        while (success):
            success, frame = cap.read()
            print("---> 正在读取第%d帧:" % frame_index, success)
            flag = FPS * n
            flag = int(flag)
            if frame_index % flag == 0 and success:
                n += 1
                resize_frame = cv2.resize(frame, (frame_width, frame_height), interpolation=cv2.INTER_AREA)
                idx = 0
                if frame_count < 10:
                    cv2.imwrite(each_video_save_full_path + "/0000%d.jpg" % frame_count, resize_frame)
                if frame_count >= 10:
                    cv2.imwrite(each_video_save_full_path + "/000%d.jpg" % frame_count, resize_frame)
                for a in alpha:
                    for b in beta:
                        idx += 1
                        resize_frame = Contrast_and_Brightness(a, b, resize_frame)
                        if frame_count < 10:
                            cv2.imwrite(each_video_save_full_path + '_{}/'.format(idx) + "0000%d.jpg" % frame_count,
                                        resize_frame)
                        if frame_count >= 10:
                            cv2.imwrite(each_video_save_full_path + '_{}/'.format(idx) + "000%d.jpg" % frame_count,
                                        resize_frame)
                frame_count += 1
            frame_index += 1
        cap.release()


def main():
    video2frame(videos_src_path, frames_save_path, width, height, time_interval)


if __name__ == '__main__':
    main()

#
#
# cap = cv2.VideoCapture(0)
#
# while (cap.isOpened()):
#     ret, frame = cap.read()  ##ret返回布尔量
#     cv2.imshow('frame', frame)
#
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     frame1 = Contrast_and_Brightness(1.3, 20, frame)
#     frame2 = Contrast_and_Brightness(1.3, -20, frame)
#     frame3 = Contrast_and_Brightness(0.8, -20, frame)
#     frame4 = Contrast_and_Brightness(0.8, 20, frame)
#
#     cv2.imshow('frame1', frame1)
#     cv2.imshow('frame2', frame2)
#     cv2.imshow('frame3', frame3)
#     cv2.imshow('frame4', frame4)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
