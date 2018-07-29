import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)
    l1.setText('Green Clown Goby')
    l2.setPixmap(QtGui.QPixmap('goby.png'))
    l1.move(100, 25)
    l2.move(100, 50)
    w.setWindowTitle('Sample GUI demo')
    w.setGeometry(200, 100,800, 500)
    w.show()
    sys.exit(app.exec_())


window()



