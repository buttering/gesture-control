import json


jsonPath = r"mode.json"


# 根据不同软件设置手势配置操作
# parameters:
#   操作模式，即软件类型,
#   模式对象，储存当前模式类型
def readMode(modeClass, modeType: str):

    with open(jsonPath) as fp:
        mode = json.load(fp)[modeType]

    for key, value in mode.items():
        setattr(modeClass, key, value)



if __name__ == '__main__':
    readMode("picture")
