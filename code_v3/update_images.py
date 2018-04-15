"""
Summary => threading to update the images in the ui.

Description => creates a thread that will update all the non-static images, in
        the ui.

Author => Matthew Howard (mah60).
Version => 0.1 - 01/04/2018 - set up the basic thread to be able to update the
                        images in the ui.
           0.2 - 15/04/2018 - changed the code to use QThread and now signals
                        the main GUI thread and calls the command
                        update_images.
                        Method developed with help from:
                        http://euanfreeman.co.uk/pyqt-qpixmap-and-threads/
                        last seen: 15/04/2018
                        Code change to support python2 instead of python3
"""

from PyQt4 import QtCore


class UpdateImages(QtCore.QThread):
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
        QtCore.QThread.__init__(self)

        self.ui = ui

    def run(self):
        """
        Summary => update all the images in the ui.

        Description => will reload all the non-static images in the ui. This
                will update the images current set values. For those images.

                This is done by sending a signal to the main gui thread,
                through signals. This method was found from:
                http://euanfreeman.co.uk/pyqt-qpixmap-and-threads/
                Last read: 15/04/2018

        args => None

        None => None
        """
        images = ["Images/takenPicture.jpg", "Images/proccessedImage.jpg"]
        self.emit(QtCore.SIGNAL("update_images(PyQt_PyObject)"), images)
