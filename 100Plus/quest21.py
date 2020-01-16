#------------------------------------------------------------------------------------# 
## A robot moves in a plane starting from the original point (0,0) ##
## The robot can move UP, DOWN, LEFT and RIGHT with given steps ##
## The trace of robot movement is shown as the following: ##
## UP 5, DOWN 3, LEFT 3, RIGHT 2 ##
## The program should compute the distance from current position and original point ##
## If the distance is a float, then just print the nearest integer. ##
#------------------------------------------------------------------------------------# 
from math import sqrt
import re

U = 0; D = 0; L = 0; R = 0
x = 0; y = 0
while True:
    coords = input('Enter coordinates:')
    if not coords:
        break
    direction = re.findall(r'[UDRL]', coords)
    magnitude = re.findall(r'\d+', coords)  
    print(direction[0])
    print(magnitude[0])
    if direction[0] == 'U':
        y = y + int(magnitude[0])
    elif direction[0] == 'D':
        y = y - int(magnitude[0])
    elif direction[0] == 'R':
        x = x + int(magnitude[0])
    elif direction[0] == 'L':
        x = x - int(magnitude[0])

print ('Final values',x, y)
distance = sqrt((x**2) + (y**2)) 
print('Distance',round(distance))