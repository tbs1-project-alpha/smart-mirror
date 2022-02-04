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
        pass
    
    # define the run method
    def run(self):
        # load the known faces and the encodings
        path = "/home/justinr/Desktop/GitKraken/smart-mirror/face_rec/knownPerson/" # Add "/" at the end of the path
        known_face_encodings = []
        known_face_names = []

        video_capture = cv2.VideoCapture(0)

        # loop over the image paths
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

        # make different variables for the known faces and the encodings
        for x in range(len(onlyfiles)):
            onlyfiles1 = f"{onlyfiles[x][:len(onlyfiles[x]) - 4]}"
            globals()['image%s' % x] = face_recognition.load_image_file(f"{path}{onlyfiles[x]}")
            globals()['face_encoding%s' % x] = face_recognition.face_encodings(globals()['image%s' % x])[0]
            known_face_encodings.append(globals()['face_encoding%s' % x])
            known_face_names.append(onlyfiles1)

        # initialize the video stream
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        # loop over the frames from the video stream
        while True:
            ret, frame = video_capture.read()  # read the frame
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # resize the frame
            rgb_small_frame = small_frame[:, :, ::-1]  # convert the frame to rgb

            if process_this_frame: # process the frame
                face_locations = face_recognition.face_locations(rgb_small_frame) # find the face locations
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) # find the face encodings

                face_names = [] # initialize the list of names for the recognized faces
                for face_encoding in face_encodings: # loop over the facial encodings
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding) # compare the face to the known faces
                    name = "Unknown" # initialize the name of the person if it is unknown

                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding) # find the distance between the face and the known faces
                    best_match_index = np.argmin(face_distances) # find the index of the best match
                    if matches[best_match_index]: # check if the face is a match for the known face
                        name = known_face_names[best_match_index] # set the name of the person to the name of the known face

                    face_names.append(name) # append the name of the person to the list of names

            process_this_frame = not process_this_frame # flip the process_this_frame variable

            for (top, right, bottom, left), name in zip(face_locations, face_names): # loop over the recognized faces
                # scale the top and bottom coordinates:
                top *= 4
                bottom *= 4

                # scale the right and left coordinates:
                left *= 4 
                right *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) # draw a rectangle around the face

                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED) # draw a rectangle around the face
                font = cv2.FONT_HERSHEY_DUPLEX # set the font
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)  # draw the name of the person

            cv2.imshow('Video', frame) # show the video

            if cv2.waitKey(1) == ord('q'): # press q to quit
                break

        video_capture.release() # release the video capture
        cv2.destroyAllWindows() # destroy all the windows


if __name__ == '__main__':
    getGui = Gui() # create the GUI
    getGui.run() # run the GUI