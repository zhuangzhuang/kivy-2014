from kivy.clock import Clock
from kivy.graphics.instructions import RenderContext
from kivy.uix.widget import Widget

from .util import load_tex_uv


class Game(Widget):
    '''Game renderer'''

    def __init__(self, **kwargs):
        self.canvas = RenderContext(use_parent_projection=True)
        self.canvas.shader.source = 'multiquad.glsl'
        Widget.__init__(self, **kwargs)

        self.tex_uv = load_tex_uv('test.atlas')

        Clock.schedule_interval(self.update_glsl, 60 ** -1)

    def update_glsl(self, nap):
        self.canvas.clear()
