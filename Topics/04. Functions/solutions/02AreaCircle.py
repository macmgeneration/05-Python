import math

def area_of_circle(r):
    return math.pi * r **2

radius = int(input('Enter radius: '))
print('The area is: ', area_of_circle(radius))