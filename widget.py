import requests
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import *
from PySide6.QtWidgets import *

from MirrorUI.datetime import DateTime
from MirrorUI.getGreeting import Greeting
from MirrorUI.weather import Weather


class MirrorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.update_delay_addons = 1000000
        self.update_delay_time = 1000

        self.greetings = Greeting(self.getName())
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

        newsfeed_timer = QTimer(self)
        newsfeed_timer.timeout.connect(self.update_newsfeed)
        newsfeed_timer.start(self.update_delay_addons)

        newspage_timer = QTimer(self)
        newspage_timer.timeout.connect(self.update_news)
        newspage_timer.start(self.update_delay_news)

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
        self.ui.news.setText(str(self.news_manager.parse_page(self.news_manager.next_page())))

    def update_newsfeed(self):
        self.news_manager.current_feed = self.news_manager.parse_feed()


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