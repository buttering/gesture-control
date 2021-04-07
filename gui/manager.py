# 在引入父目录的模块之前加上如下代码：
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import config.socketConfig as socketConfig
import server.SocketServer as socketServer
from online_demo import newtest
from model import feapoint_demo


class Manager(object):
    def __init__(self):
        object.__init__(self)
        # 讲解人员的ip地址
        self.__socketServerIp = socketConfig.IP
        self.__socketServerPort = socketConfig.PORT

    # 获取当前会议主机IP
    def getIp(self) -> str:
        return self.__socketServerIp

    # 改为在创建会议后返回会议号meetingId

    # 创建会议
    # 默认发起者为讲解人员,启动socket服务器,并返回服务器实例和会议号meetingId
    def createMeeting(self, listener):
        server = socketServer.SocketServer()
        server.runServer(listener)
        meetingId = '127.0.0.1'
        return server, meetingId

    # 通过会议号meetingId加入会议
    # 与讲解人员主机进行连接，并返回客户端实例。但并未启动手势识别功能
    def joinMeeting(self, meetingId):
        client = feapoint_demo.GestureRecognize()
        # TODO：根据会议号，向服务器获取讲解人主机ip地址
        ip = meetingId
        client.startUpClient(ip, self.__socketServerPort)
        client.main()
        return client
