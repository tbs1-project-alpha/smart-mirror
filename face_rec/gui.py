# import all the necessary modules
import face_recognition
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join


# define the class for the GUI
class Gui(object):
    # define the constructor
    def __init__(self) -> None:
        # load the known faces and the encodings
        self.path = "/home/justin/Desktop/GitKraken/smart-mirror-testing/face_rec/images" + "/"
        self.known_face_encodings = []
        self.known_face_names = []

        self.video_capture = cv2.VideoCapture(0)

        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def getNames(self):
        # loop over the image paths
        return [f for f in listdir(self.path) if isfile(join(self.path, f))]

    def addKnownFace(self, onlyfiles):
        # make different variables for the known faces and the encodings
        for x in range(len(onlyfiles)):
            onlyfiles1 = f"{onlyfiles[x][:len(onlyfiles[x]) - 4]}"
            globals()[f'image{x}'] = face_recognition.load_image_file(
                f"{self.path}{onlyfiles[x]}"
            )

            globals()[f'face_encoding{x}'] = face_recognition.face_encodings(
                globals()[f'image{x}']
            )[0]

            self.known_face_encodings.append(globals()[f'face_encoding{x}'])
            self.known_face_names.append(onlyfiles1)

    def recognize(self):
        self.ret, self.frame = self.video_capture.read()  # read the frame
        self.small_frame = cv2.resize(self.frame, (0, 0), fx=0.25, fy=0.25)  # resize the frame
        self.rgb_small_frame = self.small_frame[:, :, ::-1]  # convert the frame to rgb 

        if self.process_this_frame: # process the frame
            self.face_locations = face_recognition.face_locations(self.rgb_small_frame) # find the face locations
            self.face_encodings = face_recognition.face_encodings(self.rgb_small_frame, self.face_locations) # find the face encodings

            self.face_names = [] # initialize the list of names for the recognized faces
            for face_encoding in self.face_encodings: # loop over the facial encodings
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding) # compare the face to the known faces
                self.name = "Unknown" # initialize the name of the person if it is unknown

                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding) # find the distance between the face and the known faces
                best_match_index = np.argmin(face_distances) # find the index of the best match
                if matches[best_match_index]: # check if the face is a match for the known face
                    self.name = self.known_face_names[best_match_index] # set the name of the person to the name of the known face

                self.face_names.append(self.name) # append the name of the person to the list of names

        self.process_this_frame = not self.process_this_frame # flip the process_this_frame variable

    def drawBoxes(self):
        for (top, right, bottom, left), self.name in zip(self.face_locations, self.face_names): # loop over the recognized faces
            # scale the top and bottom coordinates:
            top *= 4
            bottom *= 4

            # scale the right and left coordinates:
            left *= 4 
            right *= 4

            cv2.rectangle(self.frame, (left, top), (right, bottom), (0, 0, 255), 2) # draw a rectangle around the face

            cv2.rectangle(self.frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED) # draw a rectangle around the face
            font = cv2.FONT_HERSHEY_DUPLEX # set the font
            cv2.putText(self.frame, self.name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)  # draw the name of the person


    # define the run method
    def run(self):
        names = self.getNames()
        self.addKnownFace(names)
        self.end()


    def end(self):

        # loop over the frames from the video stream
        while True:
            self.recognize()
            self.drawBoxes()
            cv2.imshow('Video', self.frame) # show the video

            if cv2.waitKey(1) == ord('q'): # press q to quit
                break

        self.video_capture.release() # release the video capture
        cv2.destroyAllWindows() # destroy all the windows


if __name__ == '__main__':
    getGui = Gui() # create the GUI
    getGui.run() # run the GUI