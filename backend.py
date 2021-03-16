import glfw
import contextlib
import skia
from OpenGL import GL


class GlfwWindow:
    def __init__(self, width:int=800, height:int=640):
        self.width = width
        self.height = height

    @contextlib.contextmanager
    def create_window(self):
        if not glfw.init():
            raise RuntimeError('Failed to initialize GLFW')
        glfw.window_hint(glfw.STENCIL_BITS, 8)
        self.window = glfw.create_window(self.width, self.height, '', None, None)
        glfw.make_context_current(self.window)
        yield self.window
        glfw.terminate()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value:int):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value:int):
        self._height = value
        
    @property
    def window(self):
        return self._window
    
    @window.setter
    def window(self, value):
        self._window = value


class SkiaSurface:
    def __init__(self, window:GlfwWindow):
        self.window = window

    @contextlib.contextmanager
    def create_surface(self):
        self.context = skia.GrDirectContext.MakeGL()
        self.render_target = skia.GrBackendRenderTarget(
            self.window.width,
            self.window.height,
            0,
            0,
            skia.GrGLFramebufferInfo(0, GL.GL_RGBA8)
        )
        self.surface = skia.Surface.MakeFromBackendRenderTarget(
            self.context,
            self.render_target,
            skia.kBottomLeft_GrSurfaceOrigin,
            skia.kRGBA_8888_ColorType,
            skia.ColorSpace.MakeSRGB()
        )
        assert self.surface is not None
        yield self.surface
        self.context.abandonContext()

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value

    @property
    def render_target(self):
        return self._render_target

    @render_target.setter
    def render_target(self, value):
        self._render_target = value

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, value):
        self._surface = value

    @property
    def window(self):
        return self._window

    @window.setter
    def window(self, value):
        self._window = value
