from pynput import mouse

mouse = mouse.Controller()


def scrollCtl(vertical: int, horizontal: int = 0):
    mouse.scroll(horizontal, vertical)