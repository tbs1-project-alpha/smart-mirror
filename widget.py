import requests

from PySide6.QtCore import *
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
        self.update_delay_addons = 1000000
        self.update_delay_time = 1000

        self.greetings = Greeting(self.getName())
        self.news_manager = GetNews()
        self.weather_manager = Weather()

        loader = QUiLoader()
        self.ui = loader.load("form.ui", None)
        self.ui.show()

        update_timer = QTimer(self)
        update_timer.timeout.connect(self.update)
        update_timer.start(self.update_delay_time)

        self.update_weather()
        self.update_news()
        self.update_greeting()

        greeting_timer = QTimer(self)
        greeting_timer.timeout.connect(self.update_greeting)
        greeting_timer.start(self.update_delay_addons)

        weather_timer = QTimer(self)
        weather_timer.timeout.connect(self.update_weather)
        weather_timer.start(self.update_delay_addons)

        news_timer = QTimer(self)
        news_timer.timeout.connect(self.update_news)
        news_timer.start(self.update_delay_addons)
        
    def update(self):
        self.ui.clock.setText(DateTime().get_time().strftime("%H:%M:%S"))
        self.ui.date.setText(DateTime().get_date().strftime("%d.%m.%Y"))

    def update_weather(self):
        self.image = QImage()
        self.image.loadFromData(requests.get(self.weather_manager.getIcon()).content)
        self.pixmap = QPixmap(self.image)

        self.ui.temp.setText(self.weather_manager.getTemp())
        self.ui.temp_visual.setPixmap(self.pixmap)

    def update_news(self):
        self.ui.news.setText(str(self.news_manager.report()))

    def update_greeting(self):
        self.ui.greating.setText(self.greetings.getGreeting())

    def getName(self):
        with open('face.txt') as f:
            first_line = f.readline()

        return first_line

if __name__ == "__main__":
    app = QApplication([])
    window = MirrorUI()
    app.exec_()