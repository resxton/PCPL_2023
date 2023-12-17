from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length, color):
        super().__init__(side_length, side_length, color)

    def __repr__(self):
        return "Square: side_length={}, color={}, area={}".format(
            self.width, self.color.color, self.calculate_area()
        )
