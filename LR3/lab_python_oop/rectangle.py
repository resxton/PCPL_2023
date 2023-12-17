from .geometrical_figure import GeometricalFigure
from .color import Color

class Rectangle(GeometricalFigure):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    def calculate_area(self):
        return self.width * self.height

    def __repr__(self):
        return "Rectangle: width={}, height={}, color={}, area={}".format(
            self.width, self.height, self.color.color, self.calculate_area()
        )
