from softController import jsonConfig
from softController import keyboardController
from softController import processListener
import time


class modeBean:
    """存储当前软件模式(mode)中不同手势(gesture)所对应操作(operation)"""

    # 模式名
    __modeName = ""

    # 点击手势
    click = ""
    # 向左平移手势
    panLeft = ""
    # 向右平移手势
    panRight = ""
    # 放大手势
    enlarge = ""
    # 缩小手势
    narrow = ""
    # 抓取手势
    grab = ""
    # 顺时针旋转手势
    clockwiseRotation = ""
    # 逆时针旋转手势
    counterClockwiseRotation = ""
    # 自定义手势1
    custom1 = ""
    # 自定义手势2
    custom2 = ""

    # TODO：所有属性的set和get
    def getModeName(self):
        return self.__modeName

    def setModeName(self, modeName):
        self.__modeName = modeName

    def __init__(self):
        jsonConfig.readMode(self, "init")

    # 根据模式设置操作
    def setOperation(self, mode):
        jsonConfig.readMode(self, mode)

    # 根据当前模式调用对应手势的操作
    def callOperation(self, gesture: str):
        #  这里是直接通过成员变量名获取值，所以传进参数必须严格一致
        operation = getattr(self, gesture, None)
        print("mode:",self.__modeName, "gesture:", gesture, ",operation:", operation, "is called")
        if operation == "leftCtl":
            keyboardController.leftCtl()
        elif operation == "rightCtl":
            keyboardController.rightCtl()
        elif operation == "taskCtl":
            keyboardController.taskCtl()
            self.setOperation("system")
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
            time.sleep(0.01)  # 等待焦点切换完成
            pname = processListener.active_window_process_name()
            modeType = processListener.processMap(pname)
            self.setOperation(modeType)
        elif operation == "volumeUpCtl":
            keyboardController.volumeUpCtl()
        elif operation == "volumeDownCtl":
            keyboardController.volumeDownCtl()
        elif operation == "screenGoBlackCtl":
            keyboardController.pptScreenGoBlack()


if __name__ == '__main__':
    # modeType = "tencent meeting"
    # gesture = "narrow"
    # mode = modeDAO()
    # mode.setOperation(modeType)
    # time.sleep(2)
    # mode.callOperation(gesture)
    mode = modeBean()
    print(mode.getModeName(), mode.click)
    mode.callOperation("click")
    print(mode.getModeName(), mode.click)
    time.sleep(0.5)
    mode.callOperation("panRight")
    time.sleep(0.5)
    mode.callOperation("click")
    print(mode.getModeName(), mode.click)
