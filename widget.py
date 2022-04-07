import requests

from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import *

from MirrorUI.getnews import GetNews
from MirrorUI.geotracker import GeoTracker
from MirrorUI.weather import Weather
from MirrorUI.datetime import DateTime


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui", None)
        self.ui.show()
        
        image = QImage()
        image.loadFromData(requests.get(Weather().getIcon()).content)
        pixmap = QPixmap(image)

        self.ui.clock.setText(DateTime().get_time().strftime("%H:%M:%S"))
        self.ui.date.setText(DateTime().get_date().strftime("%d.%m.%Y"))
        self.ui.greating.setText("GREETING")
        self.ui.temp.setText(Weather().getTemp())
        self.ui.temp_visual.setPixmap(pixmap)
        self.ui.news.setText("NEWS")



if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    app.exec_()