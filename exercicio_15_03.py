import sys

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def slope_from_origin(self):
        if self.x is not 0:
            return self.y/self.x
        else:
            print('Infinito')

print(Point(4,10).slope_from_origin())