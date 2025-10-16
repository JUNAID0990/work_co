# Given values
angle = 60
radius = 42
# pi = 3.14159265358979323
pi = 3.14

# Find arc length
arc_length = (angle / 360) * 2 * pi * radius

# Side of square
side = arc_length / 4

# Area of square
area = side ** 2

print("Arc Length:", arc_length)
print("Side of Square:", side)
print("Area of Square:", area)