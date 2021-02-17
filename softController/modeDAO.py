from softController import jsonConfig
from softController import keyboardController
import time

class modeDAO:

    """存储当前软件模式(mode)中不同手势(gesture)所对应操作(operation)"""

    click = ""
    panLeft = ""
    panRight = ""
    enlarge = ""
    narrow = ""
    grab = ""
    clockwiseRotation = ""
    counterClockwiseRotation = ""



    def __init__(self):
        jsonConfig.readMode(self, "init")

    def setOperation(self, gesture):
        jsonConfig.readMode(self, gesture)

    # 根据当前模式调用对应手势的操作
    def callOperation(self, gesture: str):
        operation = getattr(self, gesture, None)
        if gesture == "leftCtl":
            keyboardController.leftCtl()
        if gesture == "rightCtl":
            print("rightCtl")
            keyboardController.rightCtl()


if __name__ == '__main__':
    modeType = "ppt"
    gesture = "panLeft"
    mode = modeDAO()
    mode.setOperation(modeType)
    print(mode.panLeft)
    time.sleep(1)
    operation = getattr(mode, gesture)
    mode.callOperation(operation)