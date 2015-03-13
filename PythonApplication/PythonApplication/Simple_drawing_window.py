from PySide.QtCore import *
from PySide.QtGui import *
from Simple_drawing_window2 import *

class Simple_drawing_window(Simple_drawing_window2):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("image/rabbit.png")