import pathlib
from time import sleep

import face_rec.recognition
import face_rec.takePic


class Main(object):
    def __init__(self):
        self.path = pathlib.Path(__file__).parent.resolve()

        self.picture = face_rec.takePic.TakePicture(self.path)
        self.recognition = face_rec.recognition.Recognize(self.path)

    def run(self):
        while True:
            self.picture.check()
            sleep(0.6)
            rec = self.recognition.check()
            if "is NOT" not in rec:
                with open('face.txt', 'w') as f:
                    f.write(self.recognition.check())
            sleep(1)


if __name__ == "__main__":
    main = Main()
    main.run()
