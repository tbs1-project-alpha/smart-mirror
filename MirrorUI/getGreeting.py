from random import randint

class Greeting:
    def __init__(self, name):
        self.name = name
        self.file1 = open('MirrorUI/assets/txt/greetings.txt', 'r')
        self.Lines = self.file1.readlines()

    def getGreeting(self):
        for count, line in enumerate(self.Lines, start=1):
            if count == randint(1, len(self.Lines)):
                return f"{line.strip()} {self.name}"