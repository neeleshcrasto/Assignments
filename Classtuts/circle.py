from getarea import Area
from math import pi

radius = int(input('Enter radius '))

class Circle():
    def __init__(self, radii):
        self.radii = radii
    
    def getar(self):
        are = Area(self.radii)
        return are

    def circumference(self):
        print('Radius is ',self.radii)
        circ = int(2*pi*(self.radii))
        return circ
    
ar = Area(radius).getarea()
ci = Circle(radius).circumference()
print('Circumference is ',ci,' and Area is ','{0:.2f}'.format(ar))

