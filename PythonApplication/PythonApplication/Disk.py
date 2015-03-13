from turtle import *

class Disk(object):
   def __init__(self,name,x_pos,y_pos,height,width):
       self.name = name
       self.x_pos = x_pos
       self.y_pos = y_pos
       self.height = height
       self.width = width
       self.color = "#ff3322"

   def showdisk(self):
        fillcolor(self.color)
        pu()
        goto(self.x_pos,self.y_pos)
        pd()
        seth(0)
        begin_fill()
        fd(self.width/2)
        seth(90)
        fd(self.height)
        seth(180)
        fd(self.width)
        seth(270)
        fd(self.height)
        seth(0)
        fd(self.width/2)
        end_fill()

   def newpos(self,x,y):
        self.x_pos = x
        self.y_pos = y
   def cleardisk(self):
        seth(0)
        clear()




