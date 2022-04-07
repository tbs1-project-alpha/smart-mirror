from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui", None)
        self.ui.show()
        self.ui.clock.setText("TIME")
        self.ui.date.setText("DATE")
        self.ui.greating.setText("GREATING")
        self.ui.temp.setText("TEMP")
        self.ui.temp_visual.setText("TEMP IMAGE")
        self.ui.news.setText("NEWS")



if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    app.exec_()