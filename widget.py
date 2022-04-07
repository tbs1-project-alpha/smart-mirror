import requests
import asyncio

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import *

from MirrorUI.getnews import GetNews
from MirrorUI.weather import Weather
from MirrorUI.datetime import DateTime
from MirrorUI.getGreeting import Greeting

from time import sleep
from random import randint


class MirrorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui", None)
        self.ui.show()

        image = QImage()
        image.loadFromData(requests.get(Weather().getIcon()).content)
        pixmap = QPixmap(image)

        self.file1 = open('MirrorUI/assets/txt/greetings.txt', 'r')
        self.Lines = self.file1.readlines()

        self.ui.clock.setText(DateTime().get_time().strftime("%H:%M:%S"))
        self.ui.date.setText(DateTime().get_date().strftime("%d.%m.%Y"))
        self.ui.greating.setText(Greeting(self.getName()).getGreeting())
        self.ui.temp.setText(Weather().getTemp())
        self.ui.temp_visual.setPixmap(pixmap)
        self.ui.news.setText("NEWS")

    def getName(self):
        for count, line in enumerate(self.Lines, start=1):
            if count == randint(1, len(self.Lines)):
                return f"{line.strip()} {self.name}"

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
            self.ui.temp.setText(pixmap)
            
            await asyncio.sleep(30)


if __name__ == "__main__":
    app = QApplication([])
    window = MirrorUI()
    
    # asyncio.run(window.setDateTime())
    # asyncio.run(window.setTemp())

    app.exec_()