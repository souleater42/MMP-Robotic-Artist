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
           0.4 - 15/04/2018 - changed code to support python2 instead of
                    python3. This required me to change from threading to
                    QThread. As well, the thread now sends a signal to the
                    main gui thread and will take a thread from the main gui
                    to update the other images when this thread is complete.
                    http://euanfreeman.co.uk/pyqt-qpixmap-and-threads/ is
                    the link that I used to help develop the signal connection.
                    last_seen: 15/04/2018
           0.5 - 20/04/2018 - removed __del__ code. As it had no code inside.
"""

import cv2
import time
from PyQt4 import QtCore, QtGui


class VideoCapture(QtCore.QThread):
    """
    Summary => threading to capture video footage.

    Description => creates a thread that will continuesly capture images at
                the rate of the fps given. This will then update the image
                to display a video on the gui.

    args => None

    return => None
    """

    stopped = False

    def __init__(self, ui, update_thread):
        """
        Summary => will intialize the thread object.

        Description => intializes the thread method and connects the thread
                to the camera as cap.

        args => None

        return => None
        """
        super(VideoCapture, self).__init__()
        QtCore.QThread.__init__(self)

        self.ui = ui
        self.update_thread = update_thread

    def run(self):
        """
        Summary => runs the VideoCapture.

        Description => runs the thread through a enternal loop that will
                update the image being used to capture the video by 60/fps.
                fps is the frames per second given at creation of this object.

        args => None

        return => None
        """
        # use:
        # v4l2-ctl -d /dev/video0 --all
        # to find camera details
        self.cap = cv2.VideoCapture(0)
        time.sleep(0.1)

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
            # will slow down the camera, so it can keep up to
            # the raspberry pi processor
            # time.sleep(0.1)
            ret, frame = self.cap.read()
            if ret is True:
                # https://stackoverflow.com/questions/34232632/convert-python-
                # opencv-image-numpy-array-to-pyqt-qpixmap-image
                captured_frame = frame
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                img = QtGui.QImage(frame.data, width, height, bytesPerLine,
                                   QtGui.QImage.Format_RGB888)
                self.emit(QtCore.SIGNAL("update_capture(QImage)"), img)

        time.sleep(0.1)
        cv2.imwrite("Images/takenPicture.jpg", captured_frame)
        # cv2.imwrite("Images/vidCap.jpg", cv2.imread("Images/blank.jpg"))
        # self.cap.release()
        # cv2.destroyAllWindows()

        # update images in gui
        self.update_thread.start()
        # update = UpdateImages(self.ui)
        # update.start()
