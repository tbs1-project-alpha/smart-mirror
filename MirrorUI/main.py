from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui", None)
        self.ui.show()
        self.ui.clock.clicked.connect()

        self.num = ""

    def number(self, N):
        self.ui.textbox.setText(self.ui.textbox.text() + N)

    def number_dot(self):
        for i in self.ui.textbox.text():
            if "." in self.ui.textbox.text():
                break
            else:
                self.ui.textbox.setText(f'{self.ui.textbox.text()}.')

    def clear(self):
        self.ui.textbox.setText("")
        self.num = ""

    def sum(self):
        self.num += str(self.ui.textbox.text())
        self.num += "+"
        self.clear()

    def sub(self):
        self.num += str(self.ui.textbox.text())
        self.num += "-"
        self.clear()

    def eq(self):
        self.num += str(self.ui.textbox.text())
        self.num = str(eval(self.num))
        self.ui.textbox.setText(self.num)


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    app.exec_()
