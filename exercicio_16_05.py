import sys

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self,posn,w,h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0},{1},{2})".format(self.corner, self.width, self.height)

    def collision_detection(self, rectangle):
        result = True
        if (rectangle.corner.x < self.corner.x and (rectangle.corner.x+rectangle.width)<self.corner.x):
            result = False
        elif (rectangle.corner.x > (self.corner.x+self.width) and (rectangle.corner.x+rectangle.width)>(self.corner.x+self.width)):
            result = False
        elif (rectangle.corner.y < self.corner.y and (rectangle.corner.y+rectangle.height)<self.corner.y):
            result = False
        elif (rectangle.corner.y > (self.corner.y+self.height) and (rectangle.corner.y+rectangle.height)>(self.corner.y+self.height)):
            result = False
        return result

