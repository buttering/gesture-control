import softController.modeBean


class gestureController:

    __modeBean = softController.modeBean.modeBean()

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
