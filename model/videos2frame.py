# coding=utf-8
import os
import cv2

videos_src_path = "C:\\Users\\86135\\Desktop\\学习\\服创数据\\try\\"
# video_formats = [".MP4", ".MOV"]
frames_save_path = "C:\\Users\\86135\\Desktop\\reasult\\"
width = 176
height = 100
time_interval = 10

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
    videos = os.listdir(video_src_path)
    m = 150000
    for each_video in videos:
        print("正在读取视频：", each_video)
        each_video_name = str(m)
        m = m + 1
        os.mkdir(frame_save_path + each_video_name)
        each_video_save_full_path = os.path.join(frame_save_path, each_video_name) + "/"

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
        while(success):
            success, frame = cap.read()
            print("---> 正在读取第%d帧:" % frame_index, success)
            flag = FPS * n
            flag = int(flag)
            if frame_index % flag == 0 and success:
                n += 1
                resize_frame = cv2.resize(frame, (frame_width, frame_height), interpolation=cv2.INTER_AREA)
                if frame_count < 10:
                    cv2.imwrite(each_video_save_full_path + "0000%d.jpg" % frame_count, resize_frame)
                if frame_count >= 10:
                    cv2.imwrite(each_video_save_full_path + "000%d.jpg" % frame_count, resize_frame)
                frame_count += 1

            frame_index += 1
        cap.release()
def main():
    video2frame(videos_src_path, frames_save_path, width, height, time_interval)
if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
# import numpy as np
# import cv2
#
#
# def Contrast_and_Brightness(alpha, beta, img):
#     blank = np.zeros(img.shape, img.dtype)
#     # dst = alpha * img + (1-alpha) * blank + beta
#     dst = cv2.addWeighted(img, alpha, blank, 1 - alpha, beta)
#     return dst
#
#
# cap = cv2.VideoCapture(0)
#
# while (cap.isOpened()):
#     ret, frame = cap.read()  ##ret返回布尔量
#     cv2.imshow('frame', frame)
#
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     frame1 = Contrast_and_Brightness(1.8, 1.3, frame)
#
#     cv2.imshow('frame1', frame1)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
