import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):
        self.fcount = 0
        self.fishDict = [['Green Clown Goby'],['images/goby.png']], [['Lyretail Anthias'],[ 'images/lanthias.jpg']], [['Firefish'],[ 'images/fgoby.png']]
        self.btn1 = QtWidgets.QPushButton('Next Fishy Pic')
        self.l1 = QtWidgets.QLabel(str(self.fishDict[self.fcount][0][0]))
        self.l2 = QtWidgets.QLabel()
        self.l2.setPixmap(QtGui.QPixmap(str(self.fishDict[self.fcount][1][0])))


        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addStretch()
        self.h_box.addWidget(self.l1)
        self.h_box.addStretch()

        self.h_boxImage = QtWidgets.QHBoxLayout()
        self.h_boxImage.addStretch()
        self.h_boxImage.addWidget(self.l2)
        self.h_boxImage.addStretch()

        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addWidget(self.btn1)
        self.v_box.addLayout(self.h_box)
        self.v_box.addLayout(self.h_boxImage)

        self.setLayout(self.v_box)
        self.setWindowTitle('Fishy Viewer')

        self.btn1.clicked.connect(self.btn1_click)

        self.show()

    def btn1_click(self):
        self.fcount += 1
        if self.fcount >= 3:
            self.fcount = 0
        self.l1.setText(str(self.fishDict[self.fcount][0][0]))
        self.l2.setPixmap(QtGui.QPixmap(str(self.fishDict[self.fcount][1][0])))


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())

