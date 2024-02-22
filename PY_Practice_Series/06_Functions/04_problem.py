# 4. Function Returning Multiple Values
# **Problem:** Create a function that returns both the area and circumference of a circle given its radius.

# note:-
# pi*r**square
# 2*pi*r
import math

radius = int(input("What is your radius: "))

def circle(radius):
    area = math.pi * (radius ** 2)
    # newarea = round(area)
    circumference = 2 * math.pi * radius
    # newCircum = round(circumference)
    return area, circumference

circle_properties = circle(radius)

print("Area of the circle:", math.floor(circle_properties[0]))
print("Circumference of the circle:", math.floor(circle_properties[1]))



