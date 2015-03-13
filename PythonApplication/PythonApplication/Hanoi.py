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


