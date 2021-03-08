from config import socketConfig
from server import socketServer
from online_demo import newtest


class Interface:

    def __init__(self):
        # 讲解人员的ip地址
        self.__socketServerIp = socketConfig.IP
        self.__socketServerPort = socketConfig.PORT

    #设置会议主机所在局域网中的IP
    def setIp(self, ip: str):
        self.__socketServerIp = ip

    #获取当前会议主机IP
    def getIp(self) -> str:
        return self.__socketServerIp

    def setPort(self, port: int):
        self.__socketServerPort = port

    def getPort(self) -> int:
        return self.__socketServerPort

    # 创建会议
    # 默认发起者为讲解人员,启动socket服务器,并返回服务器实例
    def createMeeting(self):
        server = socketServer.socketServer()
        server.runServer(self.__socketServerIp, self.__socketServerPort)
        return server

    # 加入会议
    # 与讲解人员主机进行连接，并返回客户端实例。但并未启动手势识别功能
    def joinMeeting(self):
        #ip是主机IP的字符串
        client = newtest.gestureRecognize()
        client.startUpClient(self.__socketServerIp, self.__socketServerPort)
        return client


