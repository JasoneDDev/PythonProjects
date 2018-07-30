import os
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QMainWindow, QAction, qApp

# This will be a sticky note type app, we'll let the user type in a reminder note and it will save it to a file we can
# then make another app or adjust this one to display the sticky notes or something


class NotePad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = Writer()
        self.setCentralWidget(self.form_widget)

        bar = self.menuBar()

        # menus

        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # actions

        open_action = QAction('Open File', self)
        open_action.setShortcut('Ctrl+n')
        save_action = QAction('Save File', self)
        save_action.setShortcut('Ctrl+s')
        new_action = QAction('New File', self)
        new_action.setShortcut('Ctrl+n')
        quit_action = QAction('Quit', self)
        quit_action.setShortcut('Ctrl+q')

        find_action = QAction('Find', self)

        replace_action = QAction('Replace', self)

        # adding actions

        file.addActions([new_action, open_action, save_action, quit_action])

        find_menu = edit.addMenu('Find')
        find_menu.addActions([find_action, replace_action])

        # events

        file.triggered.connect(self.respond)
        quit_action.triggered.connect(self.quit_trigger)

        self.setWindowTitle('Notepad App')
        self.resize(600, 400)

        self.show()

    def quit_trigger(self):
        qApp.quit()

    def selected(self, q):
        print(q.text() + ' selected')

    def respond(self, q):
        signal = q.text()
        if signal == 'New File':
            self.form_widget.nClear()
        elif signal == 'Open File':
            self.form_widget.nOpen()
        elif signal == 'Save File':
            self.form_widget.nSave()


class Writer(QWidget):
    def __init__(self):
        super(Writer, self).__init__()
        self.text = QTextEdit(self)

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)
        self.setWindowTitle('Simple Text Editor')

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
