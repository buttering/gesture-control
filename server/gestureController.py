import softController.modeDAO


class gestureController:
    __modeDAO = softController.modeDAO.modeDAO()

    def callOperation(self, gesture: str) -> bool:
        # TODO:身份鉴权，只执行获取了焦点的操控者指令
        self.__modeDAO.callOperation(gesture)
        return True
