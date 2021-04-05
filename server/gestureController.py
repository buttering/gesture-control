import softController.modeBean


class gestureController:

    # 保有监听器，用于向状态标识窗口发送信息
    __listener = None

    def __init__(self, ModeBean):
        # 由外部传入，保持单例
        self.__modeBean = ModeBean

    def setListener(self, listener):
        self.__listener = listener

    # 为不同手势指定不同操作
    def callOperation(self, gesture: str) -> bool:
        # TODO:身份鉴权，只执行获取了焦点的操控者指令
        self.__listener.gestureChanged(gesture)
        if gesture == "like":
            # TODO：点赞效果
            pass
        elif gesture == "unlike":
            pass
        else:
            self.__modeBean.callOperation(gesture)
        return True
