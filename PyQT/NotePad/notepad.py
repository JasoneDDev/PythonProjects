import os
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog

# This will be a sticky note type app, we'll let the user type in a reminder note and it will save it to a file we can
# then make another app or adjust this one to display the sticky notes or something


class NotePad(QWidget):
    def __init__(self):
        super(NotePad, self).__init__()
        self.text = QTextEdit(self)
        self.open_btn = QPushButton('Open Note')
        self.clr_btn = QPushButton('Clear Note')
        self.save_btn = QPushButton('Save Note')

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.open_btn)
        h_layout.addWidget(self.save_btn)
        h_layout.addWidget(self.clr_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)
        self.setWindowTitle('Simple Text Editor')

        self.save_btn.clicked.connect(self.nSave)
        self.clr_btn.clicked.connect(self.nClear)
        self.open_btn.clicked.connect(self.nOpen)
        self.show()

    def nSave(self):
        filename = QFileDialog.getSaveFileName(self, 'Save Note', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            myText = self.text.toPlainText()
            f.write(myText)

    def nOpen(self):
        filename = QFileDialog.getOpenFileName(self, 'Open Note', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    def nClear(self):
        self.text.clear()

app = QApplication(sys.argv)
writer = NotePad()
sys.exit(app.exec_())
