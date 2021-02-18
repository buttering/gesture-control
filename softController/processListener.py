import win32process, win32gui
import psutil
import time


processDict = {
    "POWERPNT.EXE": "ppt",
    "ApplicationFrameHost.exe": "picture",
    "wemeetapp.exe": "tencent meeting"
}

# 获取当前焦点窗口的进程名
def active_window_process_name() -> str:
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        process = psutil.Process(pid[-1])
        print(process.name(), "is being focusing")
        return process.name()
    except:
        pass

def processMap(pname: str) -> str:
    return processDict.get(pname, "init")

if __name__ == '__main__':
    time.sleep(3)
    forWin = win32gui.GetForegroundWindow()  # 函数返回前台窗回的句柄
    pid = win32process.GetWindowThreadProcessId(forWin)  # 获得窗口所在进程ID和线程ID
    process = psutil.Process(pid[-1])  # 对进程进行封装
    name = process.name()  # 获得进程名称
    print(name)
