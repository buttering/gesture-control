import socket
import config.socketConfig as sc


def sendMsg(msg=None):
    global tcp_client
    try:
        ip_port = (sc.IP, sc.PORT)
        """
        AF_UNIX（本机通信）
        AF_INET（TCP/IP – IPv4）
        AF_INET6（TCP/IP – IPv6）
        
        SOCK_STREAM（TCP流）
        SOCK_DGRAM（UDP数据报）
        SOCK_RAW（原始套接字）
        """
        tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_client.connect(ip_port)

        while True:
            msg = input(">>>").strip()

            if not msg: continue
            if msg == "q": break
            tcp_client.sendall(msg.encode("utf-8"))
            data = tcp_client.recv(1024)
            print("服务器命令执行的结果是:", data.decode("utf-8"))

    except Exception as e:
        print(e)
    finally:
        tcp_client.close()


if __name__ == '__main__':
    sendMsg()