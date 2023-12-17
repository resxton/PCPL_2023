import math
from .geometrical_figure import GeometricalFigure
from .color import Color

class Circle(GeometricalFigure):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "Circle: radius={}, color={}, area={}".format(
            self.radius, self.color.color, self.calculate_area()
        )
