import softController.modeBean


class gestureController:
    __modeBean = softController.modeBean.modeBean()

    def callOperation(self, gesture: str) -> bool:
        # TODO:身份鉴权，只执行获取了焦点的操控者指令
        self.__modeBean.callOperation(gesture)
        return True
