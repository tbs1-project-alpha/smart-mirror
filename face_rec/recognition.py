import face_recognition
from os import listdir
from os.path import isfile, join


class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    END = '\033[0m'

class Recognize:
    def __init__(self, path) -> None:    
        self.checked = ""
        self.path = f"{path}/face_rec/images"


    def check(self):
        picture_of_test = face_recognition.load_image_file(f"{self.path}/unknown/unknown.png")
        test_face_encoding = face_recognition.face_encodings(picture_of_test)

        onlyfiles1 = ""
        onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]

        for i in onlyfiles:
            size = len(i)
            onlyfiles1 += f"{i[:size - 4]}\n"

            unknown_picture = face_recognition.load_image_file(f"{self.path}/{i}")
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

            results = face_recognition.compare_faces(test_face_encoding, unknown_face_encoding)

            # if results[0] == True:
            #     return f"{i[:size - 4]}"

            if results == True:
                self.checked += f"{Colors.OKGREEN}{i[:size - 4]} is in the picture \n{Colors.END}"
                
            else:
                self.checked += f"{Colors.FAIL}{i[:size - 4]} is NOT in the picture \n{Colors.END}"

        return self.checked

# rec = Recognize(path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(rec.check())