import json

#VSCode路径需要设置为这个
# jsonPath = r"softController/mode.json"
jsonPath = r"../softController/mode.json"


# 根据不同软件模式设置手势配置操作
# parameters:
#   模式对象，储存当前模式类型
#   操作模式，即软件类型,
def readMode(modeClass, modeType: str):
    with open(jsonPath, 'r') as fp:
        mode = json.load(fp)[modeType]

    modeClass.modeName = modeType
    for key, value in mode.items():
        setattr(modeClass, key, value)


# 根据模式和手势修改操作
def setMode(modeName: str, gesture: str, operation: str):
    with open(jsonPath, 'r+') as fp:
        modes = json.load(fp)
        modes[modeName][gesture] = operation
        jsonStr = json.dumps(modes, indent=4)
        fp.seek(0)
        fp.write(jsonStr)
        fp.truncate()


# 添加模式
def addMode(modeName: str) -> bool:
    with open(jsonPath, 'r+') as fp:
        modes = json.load(fp)
        if modeName not in modes:
            newMode = {
                "click": "",
                "panLeft": "",
                "panRight": "",
                "enlarge": "",
                "narrow": "",
                "grab": "",
                "clockwiseRotation": "",
                "counterClockwiseRotation": "",
                "custom1": "",
                "custom2": ""
            }
            modes[modeName] = newMode
            jsonStr = json.dumps(modes, indent=4)
            fp.seek(0)
            fp.write(jsonStr)
            fp.truncate()
            return True
        return False


def deleteMode(modeName) -> bool:
    with open(jsonPath, "r+") as fp:
        modes = json.load(fp)
        if modeName in modes:
            del modes[modeName]
            jsonStr = json.dumps(modes, indent=4)
            fp.seek(0)
            fp.write(jsonStr)
            fp.truncate()
            return True
        return False


if __name__ == '__main__':
    deleteMode("aaa")
