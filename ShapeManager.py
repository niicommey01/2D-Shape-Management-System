from shape2d import Shape2D


class ShapeManager:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape2D):
        """Adds a new shape to the manager"""
        self.shapes.append(shape)

    def draw_shape(self):
        """Calls draw() on all stored shapes"""
        for shape in self.shapes:
            shape.draw()

    def resize_shape(self, factor: float):
        """Resizes all shape by a given factor"""
        for shape in self.shapes:
            shape.resize(factor)

    def move_shape(self, delta_x: float, delta_y: float):
        """Moves all shapes by the given deltas"""
        for shape in self.shapes:
            shape.move(delta_x, delta_y)
