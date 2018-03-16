"""
Summary => will be used to control the camera.

Description => TODO: add description

Author => Matthew Howard (mah60).
Version => 0.1 - 12/03/2018 -
"""
import numpy as np
import cv2


class ImageProccesor(object):
    """
    Summary => will control the camera for the robotic artist.

    Description =>

    args => None

    None => None
    """
    def __init__(self):
        """
        Summary => maintain the GUI used to control the robotic artist.

        Description =>

        args => None

        None => None
        """
        self.img = cv2.imread('Images/takenPicture.bmp', 0)

    def canny_style(self):
        self.img_edges = cv2.Canny(self.img, 500, 300)
        cv2.imwrite("Images/proccessed_image.bmp", self.img_edges)
