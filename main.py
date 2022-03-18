import os
import pathlib
import face_rec.takePic
import face_rec.recognition
from time import sleep

path = pathlib.Path(__file__).parent.resolve()

picture = face_rec.takePic.TakePicture(path)
recognition = face_rec.recognition.Recognize(path)

while True:
    picture.check()
    sleep(0.6)
    print(recognition.check())
    sleep(1)