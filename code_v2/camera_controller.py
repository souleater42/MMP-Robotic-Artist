"""
Summary => will be used to control the camera.

Description => will control the camera, for the input and output proccess's.
                This will include being able to create and stop a thread that
                is produced during the process.

Author => Matthew Howard (mah60).
Version => 0.1 - 12/03/2018 - create the basic set up for controlling the
                    camera. This is creating a thread to support a video feed
                    that will be sent to the gui.
           0.2 - 18/03/2018 -  add comments to the class.

"""
import numpy as np
import cv2
from video_capture import VideoCapture


class CameraController(object):
    """
    Summary => will control the camera for the robotic artist.

    Description => will control the camera, for the input and output
                    proccess's. This will include being able to create
                    and stop a thread that is produced during the process.

    args => None

    None => None
    """

    def __init__(self):
        """
        Summary => intialize the camera.

        Description => will intialize the camera_controller and will connect
                the camera to the application.

        args => None

        None => None
        """
        self.cap = cv2.VideoCapture(0)

    def start_video_capture(self, fps):
        """
        Summary => starts the video capture and sets the fps for this.

        Description => will start the video capture. By making a thread that
                will continusly update the gui. On what is occouring.

        args => fps -> int -> the number of frames per second you want the
                                video to be captured in.

        None => None
        """
        # intialize the video_capture object, with the set fps
        self.video_capture = VideoCapture(fps)
        # start the thread to capture the video.
        self.video_capture.start()

    def stop_video_capture(self):
        """
        Summary => stops the video_capture.

        Description => will stop the video capture by changing the static
                    boolean VideoCapture.stooped to ture.

        args => None

        None => None
        """
        # changes static boolean to true, this stops the thread running in the
        # the background
        VideoCapture.stopped = True
