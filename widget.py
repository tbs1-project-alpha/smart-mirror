import requests
import asyncio

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import *

from MirrorUI.getnews import GetNews
from MirrorUI.weather import Weather
from MirrorUI.datetime import DateTime
from MirrorUI.getGreeting import Greeting


class MirrorUI(QMainWindow):
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
        self.ui.greating.setText(self.getGreeting())
        self.ui.temp.setText(Weather().getTemp())
        self.ui.temp_visual.setPixmap(pixmap)
        self.ui.news.setText(str(GetNews().report()))

    def getName(self):
        with open('face.txt') as f:
            first_line = f.readline()

        return first_line

    def getGreeting(self):
        r = Greeting(self.getName())
        return r.getGreeting()

    async def setDateTime(self):
        while True:
            self.ui.date.setText(DateTime().get_date().strftime("%d.%m.%Y"))
            self.ui.clock.setText(DateTime().get_time().strftime("%H:%M:%S"))
            await asyncio.sleep(1)

    async def setTempNews(self):
        while True:
            self.ui.temp.setText(Weather().getTemp())

            image = QImage()
            image.loadFromData(requests.get(Weather().getIcon()).content)
            pixmap = QPixmap(image)
            self.ui.temp.setText(pixmap)
            
            self.ui.news.setText(str(GetNews().report()))
            
            await asyncio.sleep(30)


if __name__ == "__main__":
    app = QApplication([])
    window = MirrorUI()
    
    # asyncio.run(window.setDateTime())
    # asyncio.run(window.setTemp())

    app.exec_()