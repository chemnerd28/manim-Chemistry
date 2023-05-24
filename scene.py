from manim import *
from manim_Chemistry import *

class DrawCarbonElement(Scene):
    def construct(self):
        carbon = MElementObject.ElementData(atomic_number=15)
        self.add(carbon)

class DrawPeriodicTable(Scene):
    def construct(self):
        self.add(PeriodicTable(data_file=".\\manim-Chemistry\\assets\\Elements_EN.csv"))