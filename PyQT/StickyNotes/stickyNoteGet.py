import os
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog

# This will be a sticky note type app, we'll let the user type in a reminder note and it will save it to a file we can
# then make another app or adjust this one to display the sticky notes or something


class NotePad(QWidget):
    def __init__(self):
        super(NotePad, self).__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear Note')
        self.save_btn = QPushButton('Save Note')

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.save_btn)
        self.h_layout.addWidget(self.clr_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(self.h_layout)

        self.setLayout(v_layout)
        self.setWindowTitle('Sticky Note Creator')

        self.save_btn.clicked.connect(self.nSave)
        self.clr_btn.clicked.connect(self.nClear)
        self.show()

    def nSave(self):
        with open('stickyNotes.txt', 'r+') as f:
            myText = '\n' + self.text.toPlainText()
            f.write(myText)
        self.text.clear()

    def nClear(self):
        self.text.clear()


app = QApplication(sys.argv)
writer = NotePad()
sys.exit(app.exec_())
