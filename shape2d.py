from abc import ABC, abstractmethod

class Shape2D:
    @abstractmethod
    def draw(self):
        """Displays the shape's details"""
        pass

    @abstractmethod
    def resize(self, factor: float):
        """Scales the shape by a given factor"""
        pass

    @abstractmethod
    def move(self, delta_x: float, delta_y: float):
        """Adjusts the shape's position."""
        pass