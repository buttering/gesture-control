from pynput import keyboard
import softController.mouseController as mouseController

# 模拟键盘控制

# 创建键盘实例
kb = keyboard.Controller()


def main():
    # 创建监听
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release
    )as listener:
        listener.join()


def on_press(key):
    if key == keyboard.KeyCode.from_char('s'):
        pictureEnlargeCtl()
    print('{0} 被按下'.format(key))


def on_release(key):
    print('{0} 被释放'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def pagedownCtl():
    with kb.pressed(
            keyboard.Key.page_down
    ): pass


def pageupCtl():
    with kb.pressed(
            keyboard.Key.page_down
    ): pass


def upCtl():
    with kb.pressed(
            keyboard.Key.page_down
    ): pass


def downCtl():
    with kb.pressed(
            keyboard.Key.page_down
    ): pass


def leftCtl():
    with kb.pressed(
            keyboard.Key.page_down
    ): pass


def rightCtl():
    print("right key is pressed")
    with kb.pressed(
            keyboard.Key.right
    ): pass


# 任务视图，win键+tab键
def taskCtl():
    print("cmd and tab are pressed")
    with kb.pressed(
            keyboard.Key.cmd,
            keyboard.Key.tab
    ): pass


def homeCtl():
    with kb.pressed(
            keyboard.Key.home
    ): pass


def endCtl():
    with kb.pressed(
            keyboard.Key.end
    ): pass


def printScreenCtl():
    with kb.pressed(
            keyboard.Key.print_screen
    ): pass


# 控制图片放大，ctrl键+鼠标滚轮
def pictureEnlargeCtl(step: int = 4):
    kb.press(keyboard.Key.ctrl)
    mouseController.scrollCtl(step)
    kb.release(keyboard.Key.ctrl)


def pictureNarrowCtl(step: int = 4):
    kb.press(keyboard.Key.ctrl)
    mouseController.scrollCtl(-step)
    kb.release(keyboard.Key.ctrl)


# 将图片拷贝进剪贴板，ctl+c
def pictureCopyCtl():
    with kb.pressed(
            keyboard.Key.ctrl,
            keyboard.KeyCode.from_char('c')
    ): pass


# 控制图片顺时针旋转，ctr+r
def pictureClockWiseRotationCtl():
    with kb.pressed(
            keyboard.Key.ctrl,
            keyboard.KeyCode.from_char("r")
    ): pass


def enterCtl():
    with kb.pressed(
            keyboard.Key.enter
    ): pass


# 增大系统音量，fn+f3
def volumeUpCtl(step: int = 5):
    for i in range(step):
        with kb.pressed(
                keyboard.Key.media_volume_up
        ): pass


def volumeDownCtl(step: int = 5):
    for i in range(step):
        with kb.pressed(
                keyboard.Key.media_volume_down
        ): pass


if __name__ == '__main__':
    main()
