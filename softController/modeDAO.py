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

    # 根据模式设置操作
    def setOperation(self, mode):
        jsonConfig.readMode(self, mode)

    # 根据当前模式调用对应手势的操作
    def callOperation(self, gesture: str):
        operation = getattr(self, gesture, None)
        print("operation:", operation, "is called")
        if operation == "leftCtl":
            keyboardController.leftCtl()
        elif operation == "rightCtl":
            keyboardController.rightCtl()
        elif operation == "taskCtl":
            keyboardController.taskCtl()
        elif operation == "endCtl":
            keyboardController.endCtl()
        elif operation == "homeCtl":
            keyboardController.homeCtl()
        elif operation == "printScreenCtl":
            keyboardController.printScreenCtl()
        elif operation == "pictureEnlargeCtl":
            keyboardController.pictureEnlargeCtl()
        elif operation == "pictureNarrowCtl":
            keyboardController.pictureNarrowCtl()
        elif operation == "pictureCopyCtl":
            keyboardController.pictureCopyCtl()
        elif operation == "pictureClockWiseRotationCtl":
            keyboardController.pictureClockWiseRotationCtl()
        elif operation == "enterCtl":
            keyboardController.enterCtl()
        elif operation == "volumeUpCtl":
            keyboardController.volumeUpCtl()
        elif operation == "volumeDownCtl":
            keyboardController.volumeDownCtl()


if __name__ == '__main__':
    modeType = "tencent meeting"
    gesture = "narrow"
    mode = modeDAO()
    mode.setOperation(modeType)
    time.sleep(2)
    mode.callOperation(gesture)
