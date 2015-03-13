from turtle import *

class Pole:
    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.stack = []
        self.top_pos = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.thickness = 5
        self.length = 20
        self.color = "#3311FF"

    def showpole(self):
        penup()
        goto(self.x_pos, self.y_pos)
        pendown()

        color(self.color)
        setheading(0)

        forward(self.thickness/2)
        left(90)
        forward(self.length)
        left(90)
        forward(self.thickness)
        left(90)
        forward(self.length)
        left(90)
        forward(self.thickness/2)

        penup()

    def pushdisk(self, disk):
        self.stack.append(disk)
        
        disk.showdisk()

    def popdisk(self):
        for i in self.stack:
            i.cleardisk()

        self.showpole()

        ret = self.stack.pop()

        for i in self.stack:
            i.showdisk()

        return ret


