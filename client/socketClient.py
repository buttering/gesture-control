import socket
import config.socketConfig as sc
import time


class socketClient:

    __device_id = "sd545d4fs4df8sdf4"
    # TODO：获取设备唯一标识

    # 可用手势列表
    __gesture_list = ["click", "panLeft", "panRight", "enlarge", "narrow",
                      "grasp", "cwr", "ccwr", "like", "unlike"]

    # 保存tcp client实例
    __tcp_client = None

    # 启动客户端与服务器的连接
    def startUp(self, ip: str, port: int) -> bool:

        try:
            self.__tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__tcp_client.connect((ip, port))
            return True
        except Exception as e:
            print(e)
            return False

    # 关闭连接
    def shutDown(self):
        self.__tcp_client.close()


    # 生成操作接口字段
    def gesture_interface_field(self, gestureName: str, deviceid: str):
        field = '''
            {
                "interface":"gesture",
                "info":{
                    "gesturename":"''' + gestureName + '''",
                    "deviceid":"''' + deviceid + '''"
                }
            }
        '''
        return field

    # 生成焦点接口字段
    def focus_interface_field(self, deviceid: str):
        field = '''
            {
                "interface":"controlFocus",
                "info":{
                    "deviceid":"''' + deviceid + '''"
                }
            }
        '''
        return field

    # 生成注册接口字段
    def attach_interface_field(self, deviceid: str):
        field = '''
            {
                "interface":"attach",
                "info":{
                    "deviceid":"''' + deviceid + '''"
                    
                }
            }
        '''
        return field

    # 过滤特定手势，并进行网络传输
    def gestureFilter(self, gesture: str):
        if gesture in self.__gesture_list:
            print(f"检测到{gesture}手势，向服务器发送请求")
            self.sendMsg(self.gesture_interface_field(gesture, self.__device_id))


    def sendMsg(self, msg=None):
        try:
            """
            AF_UNIX（本机通信）
            AF_INET（TCP/IP – IPv4）
            AF_INET6（TCP/IP – IPv6）
            
            SOCK_STREAM（TCP流）
            SOCK_DGRAM（UDP数据报）
            SOCK_RAW（原始套接字）
            """
            #
            # self.tcp_client.sendall('{"interface":"gesture","info":{"gesturename":"click", "deviceid": "ABc"}}'.encode("utf-8"))
            # time.sleep(1)
            # self.tcp_client.sendall('{"interface":"gesture","info":{"gesturename":"panRight", "deviceid": "ABc"}}'.encode("utf-8"))
            # time.sleep(0.5)
            # self.tcp_client.sendall('{"interface":"gesture","info":{"gesturename":"click", "deviceid": "ABc"}}'.encode("utf-8"))
            self.__tcp_client.sendall(msg.encode("utf-8"))
            data = self.__tcp_client.recv(1024)
            print("服务器返回数据是:", data.decode("utf-8"))

        except Exception as e:
            print(e)



if __name__ == '__main__':
    socketClient = socketClient()
    socketClient.startUp(sc.IP, sc.PORT)
    # socketClient.gestureFilter("click")
    while True:
        msg = input(">>>").strip()
        if not msg: continue
        if msg == "q": break
        socketClient.sendMsg(msg)
    socketClient.shutDown()