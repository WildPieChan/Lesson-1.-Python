# Write a program that takes the coordinates of two points as 
# input and finds the distance between them in 2D space.

import math

print('Point A coordinate')
x1 = float(input('Enter X: '))
y1 = float(input('Enter Y: '))

print('Point B coordinate')
x2 = float(input('Enter X: '))
y2 = float(input('Enter Y: '))

AB = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

print('Distance between two points A and B is {0:.2f}'.format(AB))