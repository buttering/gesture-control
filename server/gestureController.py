import softController.modeBean


class gestureController:

    def __init__(self, ModeBean):
        # 由外部传入，保持单例
        self.__modeBean = ModeBean

    # 为不同手势指定不同操作
    def callOperation(self, gesture: str) -> bool:
        # TODO:身份鉴权，只执行获取了焦点的操控者指令
        if gesture == "like":
            # TODO：点赞效果
            pass
        elif gesture == "unlike":
            pass
        else:
            self.__modeBean.callOperation(gesture)
        return True
