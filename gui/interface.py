

class Interface:
    def __init__(self):
        pass

    #设置会议主机的局域网IP
    def setIp(self, ip):
        pass

    #获取当前会议主机IP
    def getIp(self):
        return "123.45.67.78"

    #创建会议
    def createMeeting(self):
        pass

    #加入会议
    def joinMeeting(self,ip):
        #ip是主机IP的字符串
        pass
