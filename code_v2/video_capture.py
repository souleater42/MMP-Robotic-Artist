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
           0.3 - 01/04/2018 -  this class now has the ui being passed to it.
                    This then allows us to continusly update the ui images on
                    run time. Also has a image_update method passed to it.
"""

import cv2
import threading
from PyQt5 import QtCore, QtGui
from update_images import UpdateImages


class VideoCapture(threading.Thread):
    """
    Summary => threading to capture video footage.

    Description => creates a thread that will continuesly capture images at
                the rate of the fps given. This will then update the image
                to display a video on the gui.

    args => None

    None => None
    """

    stopped = False

    def __init__(self, ui, update_method):
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
        self.update_method = update_method

    def run(self):
        """
        Summary => runs the VideoCapture.

        Description => runs the thread through a enternal loop that will
                update the image being used to capture the video by 60/fps.
                fps is the frames per second given at creation of this object.

        args => None

        None => None
        """
        # use:
        # v4l2-ctl -d /dev/video0 --all
        # to find camera details
        self.cap = cv2.VideoCapture(0)

        captured_frame = None
        # run loop until stactic variable stopped is changed to true
        while not VideoCapture.stopped:
            # check if opened, if not open the capture
            if self.cap.isOpened() is False:
                self.cap.open(0)
            # print("capture video")
            # capture the camera frame
            # ret => boolean - this is true if the frame has been read
            # correctly
            ret, frame = self.cap.read()
            if ret is True:
                cv2.imwrite("Images/vidCap.jpg", frame)
                pixmap = QtGui.QPixmap("Images/vidCap.jpg")
                pixmap = pixmap.scaled(498, 300, QtCore.Qt.KeepAspectRatio)
                self.ui.video_capture.setPixmap(pixmap)
                self.ui.video_capture.setAlignment(QtCore.Qt.AlignCenter)

                captured_frame = frame

        cv2.imwrite("Images/takenPicture.jpg", captured_frame)
        cv2.imwrite("Images/vidCap.jpg", cv2.imread("Images/blank.jpg"))
        self.cap.release()
        cv2.destroyAllWindows()

        # update images in gui
        update = UpdateImages(self.ui)
        update.start()
