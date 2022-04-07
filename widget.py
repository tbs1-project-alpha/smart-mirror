import requests
import asyncio

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import *

from MirrorUI.getnews import GetNews
from MirrorUI.weather import Weather
from MirrorUI.datetime import DateTime

from time import sleep


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

    async def setDateTime(self):
        print("start1")
        while True:
            print("run1")
            self.ui.date.setText(DateTime().get_date().strftime("%d.%m.%Y"))
            self.ui.clock.setText(DateTime().get_time().strftime("%H:%M:%S"))
            await asyncio.sleep(1)

    async def setTemp(self):
        print("start2")
        while True:
            print("run2")
            self.ui.temp.setText(Weather().getTemp())

            image = QImage()
            image.loadFromData(requests.get(Weather().getIcon()).content)
            pixmap = QPixmap(image)
            self.ui.temp.setText(Weather().getTemp())
            
            await asyncio.sleep(30)

if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    app.exec_()
    
    asyncio.run(window.setDateTime())
    asyncio.run(window.setTemp())