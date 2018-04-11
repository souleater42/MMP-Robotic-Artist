"""
Summary => threading to update the images in the ui.

Description => creates a thread that will update all the non-static images, in
        the ui.

Author => Matthew Howard (mah60).
Version => 0.1 - 01/04/2018 - set up the basic thread to be able to update the
                        images in the ui.
"""

import threading
from PyQt5 import QtCore, QtGui


class UpdateImages(threading.Thread):
    """
    Summary => will update the non-static images in the ui.

    Description => will update the non-static images in the ui.

    args => None

    None => None
    """

    def __init__(self, ui):
        """
        Summary => will intialize the thread object.

        Description => intializes the thread method and assigns the ui to this
                thread.

        args => ui - this is the ui object for the gui_view

        None => None
        """
        super(UpdateImages, self).__init__()
        threading.Thread.__init__(self)

        self.ui = ui

    def run(self):
        """
        Summary => update all the images in the ui.

        Description => will reload all the non-static images in the ui. This
                will update the images current set values. For those images.

        args => None

        None => None
        """
        pixmap = QtGui.QPixmap('Images/takenPicture.jpg')
        pixmap = pixmap.scaled(498, 300, QtCore.Qt.KeepAspectRatio)
        self.ui.captured_image.setPixmap(pixmap)
        self.ui.captured_image.setAlignment(QtCore.Qt.AlignCenter)

        pixmap = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
        self.ui.image_your_picture.setPixmap(pixmap)

        pixmap = QtGui.QPixmap('Images/proccessedImage.jpg')
        pixmap = pixmap.scaled(498, 300, QtCore.Qt.KeepAspectRatio)
        self.ui.styled_image.setPixmap(pixmap)
        self.ui.styled_image.setAlignment(QtCore.Qt.AlignCenter)
