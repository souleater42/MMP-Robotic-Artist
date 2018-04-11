"""
Summary => threading to capture video footage.

Description => creates a thread that will continuesly capture images at
            the rate of the fps given. This will then update the image
            to display a video on the gui.

Author => Matthew Howard (mah60).
Version => 0.1 - 12/03/2018 - create the basic set up for the VideoCapture.
                    with the init method and run method.
           0.2 - 15/03/2018 - added te static variable stopped, to be able to
                    stop the feed in other classes when asked.
"""
import numpy as np
import cv2
import threading


class VideoCapture(threading.Thread):
    """
    Summary => threading to capture video footage.

    Description => creates a thread that will continuesly capture images at
                the rate of the fps given. This will then update the image
                to display a video on the gui.

    args => None

    None => None
    """

    def __init__(self, ui):
        """
        Summary => will intialize the thread object.

        Description => intializes the thread method and connects the thread
                to the camera as cap.

        args => fps - int - the number of frames per second that you want the
                        image to at.

        None => None
        """
        super(VideoCapture, self).__init__()
        threading.Thread.__init__(self)
        self.ui = ui

    def run(self):
        """
        Summary => runs the VideoCapture.

        Description => runs the thread through a enternal loop that will
                update the image being used to capture the video by 60/fps.
                fps is the frames per second given at creation of this object.

        args => None

        None => None
        """
