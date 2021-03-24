import glfw
import contextlib
import skia
from OpenGL import GL


class GlfwWindow:
    def __init__(self, width:int=800, height:int=640):
        self.width = width
        self.height = height
        glfw.window_hint(glfw.STENCIL_BITS, 8)
        self.window = glfw.create_window(self.width,
                                         self.height,
                                         '',
                                         None, None)
        glfw.make_context_current(self.window)

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
    def window(self) -> glfw._GLFWwindow:
        return self._window
    
    @window.setter
    def window(self, value: glfw._GLFWwindow):
        self._window = value


class SkiaSurface:
    def __init__(self, window: GlfwWindow):
        self.window = window
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

    @property
    def context(self) -> skia.GrDirectContext:
        return self._context

    @context.setter
    def context(self, value: skia.GrDirectContext):
        self._context = value

    @property
    def render_target(self) -> skia.GrBackendRenderTarget:
        return self._render_target

    @render_target.setter
    def render_target(self, value: skia.GrBackendRenderTarget):
        self._render_target = value

    @property
    def surface(self) -> skia.Surface:
        return self._surface

    @surface.setter
    def surface(self, value: skia.Surface):
        self._surface = value

    @property
    def window(self) -> GlfwWindow:
        return self._window

    @window.setter
    def window(self, value: GlfwWindow):
        self._window = value
