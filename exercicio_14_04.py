import sys

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def get_line_to(self,point):
        a = (self.y - point.y)/(self.x - point.x)
        b = self.y - a*self.x
        return (a,b)

print(Point(4,11).get_line_to(Point(6,15)))