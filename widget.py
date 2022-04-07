# This Python file uses the following encoding: utf-8
import os
import sys
import asyncio

from pathlib import Path

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

# from face_rec.gui import GUI
# from MirrorUI.getnews import GetNews
# # from MirrorUI.getgreeting import GetGreeting
# from main import Main


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()

    sys.exit(app.exec_())
