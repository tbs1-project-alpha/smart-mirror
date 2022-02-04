# Python program to capture a single image
# using pygame library

# importing the pygame library
import pygame, pygame.camera, os, time


class TakePicture:
    def __init__(self, path) -> None:
        # initializing the camera
        pygame.camera.init()
        # make the list of all available cameras
        self.camlist = pygame.camera.list_cameras()
        # define the path where the images will be saved
        self.path = f"{path}/face_rec/knownPerson/unknown/"
        # initializing the cam variable with default camera
        self.cam = pygame.camera.Camera(self.camlist[0], (640, 480))
        # opening the camera
        self.cam.start()

    def check(self):
        # if camera is detected or not
        if self.camlist:
            self.take()
        # if camera is not detected the moving to else part
        else:
            print("No camera on current device")

        
    def take(self):
        # capturing the single image
        image = self.cam.get_image()
        # saving the image
        pygame.image.save(image, f"{self.path}unknown.png")

# app = TakePicture(path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# app.check()