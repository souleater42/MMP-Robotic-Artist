"""
Summary => will be used to control the camera.

Description => TODO: add description

Author => Matthew Howard (mah60).
Version => 0.1 - 12/03/2018 -
"""
import numpy as np
import cv2
import threading
from video_capture import VideoCapture


class CameraController(object):
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
        self.cap = cv2.VideoCapture(0)
        self.video_capture = VideoCapture()

    def start_video_capture(self):
        """
        Summary => maintain the GUI used to control the robotic artist.

        Description =>

        args => None

        None => None
        """
        self.video_capture.start()

    def stop_video_capture(self):
        """
        Summary => maintain the GUI used to control the robotic artist.

        Description =>

        args => None

        None => None
        """
        VideoCapture.stopped = True
