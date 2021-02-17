from pynput import keyboard

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
        pagedownCtl()
    print('{0} 被按下'.format(key))


def on_release(key):
    print('{0} 被释放'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def pagedownCtl():
    with kb.pressed(
            keyboard.Key.page_down
    ):
        pass


def pageupCtl():
    with kb.pressed(
            keyboard.Key.page_down
    ):
        pass


def upCtl():
    with kb.pressed(
            keyboard.Key.page_down
    ):
        pass


def downCtl():
    with kb.pressed(
            keyboard.Key.page_down
    ):
        pass


def leftCtl():
    with kb.pressed(
            keyboard.Key.page_down
    ):
        pass


def rightCtl():
    print("right key")
    with kb.pressed(
            keyboard.Key.right
    ):
        pass


if __name__ == '__main__':
    main()
