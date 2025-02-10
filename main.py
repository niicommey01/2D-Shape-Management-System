from Rectangle import Rectangle
from ShapeManager import ShapeManager


# Create Shape
rectangle1 = Rectangle("Red", 2, 3,  5, 10)

# Add shape to ShapeManager
manager = ShapeManager()
manager.add_shape(rectangle1)

# Draw shape
print("Initial shape: ")
manager.draw_shape()

# Resize shape
print("Resized shape:")
manager.resize_shape(2.0)
manager.draw_shape() # Draw again to see the resized shape

# Move rectangle
print("Moved shape:")
manager.move_shape(-1.0, 1.0)
manager.draw_shape() # Draw again to see the moved shape