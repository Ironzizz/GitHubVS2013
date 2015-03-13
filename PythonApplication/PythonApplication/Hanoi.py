from turtle import *
from Disk import *
from Pole import *

class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startPole = Pole(start, 0, 0)
        self.workspacePole = Pole(workspace, 150, 0)
        self.destinationPole = Pole(destination, 300, 0)
        self.startPole.showpole()
        self.workspacePole.showpole()
        self.destinationPole.showpole()
        for i in range(n):
            self.startPole.pushdisk(Disk("d"+str(i), 0, i*150, 20, (n-i)*30))

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n==1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1, s, w, d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)

    def solve(self):
        self.move_tower(3, self.startPole, self.destinationPole, self.workspacePole)

h=Hanoi()
h.solve()


