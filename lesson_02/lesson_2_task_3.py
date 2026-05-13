import math


def square(side):
    area = side * side
    return math.ceil(area)


side = 2.1
result = square(side)
print(f"Площадь квадрата со стороной {side}: {result}")
