from math import pi

class Area(object):
    def __init__(self, radii):
        self.radii = radii

    def getarea(self):
        area = pi*(self.radii**2)
        return area
