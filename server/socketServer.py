import socketserver
import config.socketConfig as sc

ip_port = (sc.IP, sc.PORT)


class MyServer(socketserver.BaseRequestHandler):
    # 重写handle方法，决定每一个连接过来的操作
    def handle(self):
        """
        self.request属性是套接字对象, 所以使用self.request.xxxx调用套接字的函数
        self.server包含调用处理程序的实例
        self.client_address是客户端地址信息
        """

        while True:
            try:
                # 接受消息
                data = self.request.recv(1024)
                if not data: break
                print("收到客户端的消息是", data.decode("utf-8"))
                # 发送消息
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)
                break

    def setup(self) -> None:
        print("新建连接")
        print("conn is :", self.request)  # conn
        print("addr is :", self.client_address)  # addr

if __name__ == '__main__':
    # 定义服务端类型:支持ipv4的TCP协议的服务器
    s = socketserver.ThreadingTCPServer(ip_port, MyServer)
    # 持续循环运行
    s.serve_forever()
