from abc import ABC

from shape2d import Shape2D

class Rectangle(Shape2D, ABC):
    def __init__(self, color: str, position_x: float, position_y: float, width: float, height: float):
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height

    def draw(self):
        """Prints rectangle"""
        print(f"Colour: {self.color}\n"
              f"Position: ({self.position_x}, {self.position_y})\n"
              f"Width: {self.width}\n"
              f"Height: {self.height}\n")

    def resize(self, factor: float):
        """Scales width and height by factor"""
        self.width += factor
        self.height += factor

    def move(self, delta_x: float, delta_y: float):
        """Adjusts the rectangle's position"""
        self.position_x += delta_x
        self.position_y += delta_y