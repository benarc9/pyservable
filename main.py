import skia
import contextlib
from backend import GlfwWindow, SkiaSurface
from components.panel import Panel
from lib import Vector
import glfw

@contextlib.contextmanager
def main():
    panel = Panel(Vector(20, 20), Vector(40, 40), skia.ColorYELLOW)
    glfw.init()
    window = GlfwWindow()
    surface = SkiaSurface(window)

    while (glfw.get_key(window.window, glfw.KEY_ESCAPE) != glfw.PRESS
           and not glfw.window_should_close(window.window)):
        surface.surface.flushAndSubmit()
        panel.draw(surface.surface.getCanvas())
        glfw.swap_buffers(window.window)
        glfw.wait_events()










if __name__ == '__main__':
    main()

