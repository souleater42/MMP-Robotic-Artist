"""
Summary => will be used to control the camera.

Description => TODO: add description

Author => Matthew Howard (mah60).
Version => 0.1 - 12/03/2018 -
"""
import numpy as np
import cv2
import threading


class VideoCapture(threading.Thread):
    """
    Summary => will control the camera for the robotic artist.

    Description =>

    args => None

    None => None
    """
    stopped = False

    def __init__(self):
        """
        Summary => maintain the GUI used to control the robotic artist.

        Description =>

        args => None

        None => None
        """
        super(VideoCapture, self).__init__()
        threading.Thread.__init__(self)
        self.cap = cv2.VideoCapture(0)

    def run(self):
        """
        Summary => maintain the GUI used to control the robotic artist.

        Description =>

        args => None

        None => None
        """
        while not VideoCapture.stopped:
            #print("capture video")
            x = x

    def stop(self):
        """
        Summary => maintain the GUI used to control the robotic artist.

        Description =>

        args => None

        None => None
        """
        print("stop video capture")
        self._stop_event.set()
