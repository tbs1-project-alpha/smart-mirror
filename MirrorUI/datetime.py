# exercise:
# write a program that prints the date and time

import datetime


class DateTime:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.time = datetime.datetime.now()

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_date_time(self):
        return self.date, self.time