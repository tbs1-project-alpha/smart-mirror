import os
import pathlib
import face_rec.takePic
import face_rec.recognition
from time import sleep


class Main(object):
    def __init__(self):
        self.path = pathlib.Path(__file__).parent.resolve()

        self.picture = face_rec.takePic.TakePicture(self.path)
        self.recognition = face_rec.recognition.Recognize(self.path)

    def run(self):
        self.picture.check()
        sleep(0.6)
        print(self.recognition.check())
        sleep(1)


if __name__ == "__main__":
    main = Main()
    main.run()