#1
import math

degree = 15
radian = degree * (math.pi / 180)

print("Output radian:", radian)

#2
import math
height = 5
base1 = 5
base2 = 6

area = 0.5 * (base1 + base2) * height

print("Output:", area)

#3
import math

num_sides = 4
side_length = 25

area = int(num_sides * side_length ** 2 / (4 * math.tan(math.pi / num_sides)))

print("The area of the polygon is:", area)

#4
import math
base_length = 5
height = 6

area = base_length * height

print("Output:", "{:.1f}".format(area))

