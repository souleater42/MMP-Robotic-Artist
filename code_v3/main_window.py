"""
Summary => Will be used to control and generate a GUI.

Description => This class will be used to generate and control the GUI used
for the system. You will be able to control the camera and see the feed
comming from it.

Author => Matthew Howard (mah60).
Version => 0.1 - 12/03/2018 - has the basic set up for the gui. Created Actions
                        to control the transactions in the gui and the class is
                        able to draw the gui design from gui_view made in qt
                        designer.
           0.2 - 15/03/2018 -> 01/04/2018 - added muiltiple actions for the
                        individula buttons in the ui. This includes actions to
                        change pages and take pictures.
           0.3 - 15/04/2018 - changed the code to support python2.7, This
                        involved; -changing from pyqt5 - pyqt4.
                                  -Made the update_images method, which is
                                   triggered through signals from the
                                   update_images QThread.
                                  -new method called update_capture,
                                   this will be the method to create a signal
                                   to update the capture in the main gui.
"""
import sys
from camera_controller import CameraController
from video_capture import VideoCapture
from image_proccesor import ImageProccesor
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMessageBox
from gui_view import Ui_mainWindow
from plotter_controller import PlotterController
from update_images import UpdateImages
import cv2

from dithering import Dithering
from dithering_plotter import DitheringPlotter

import time


class MainWindow(QtGui.QMainWindow):
    """
    Summary => maintain the GUI used to control the robotic artist.

    Description =>

    Args => None

    Return => None
    """

    def __init__(self):
        """
        Summary => initialize the main window view.

        Description =>

        Args => None

        Return => None
        """
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.move(100, 100)  # move gui to the 100,100 on the screen
        self.setWindowIcon(QtGui.QIcon('Images/Icon.png'))  # sets icon for gui
        self.camera = CameraController(self.ui)
        # --------------------------------------------------------
        # set menuBar actions
        self.ui.actionExit_Application.setShortcut('Ctrl+Q')
        self.ui.actionExit_Application.setStatusTip('Leaving Application')
        self.ui.actionExit_Application.triggered.connect(
                                                        self.close_application)
        # --------------------------------------------------------
        # set the stackedWidget view to be the first page
        self.display_stack(0)
        # --------------------------------------------------------
        # set up buttons
        self.ui.capture_picture.clicked.connect(self.capture_image)
        btn = self.ui.yes_no_button.button(self.ui.yes_no_button.Yes)
        btn.clicked.connect(self.accept_picture)
        btn = self.ui.yes_no_button.button(self.ui.yes_no_button.No)
        btn.clicked.connect(self.reject_picture)
        # self.ui.yes_no_button.clicked.connect(self.accept_picture)
        btn = self.ui.yes_no_button2.button(self.ui.yes_no_button.Yes)
        btn.clicked.connect(self.start_plot)
        self.ui.btn_continue1.clicked.connect(self.proccess_image)
        btn = self.ui.yes_no_button2.button(self.ui.yes_no_button.No)
        btn.clicked.connect(self.reject_style)
        # self.ui.video_capture.show()

# ------------------------------------------------------------
# functions
# ------------------------------------------------------------

    def display_stack(self, i):
        """
        Summary => changes the widget stack page.

        Description => will change the stacked widget view to the int given
        through i.

        This code was found on:
        https://www.tutorialspoint.com/pyqt/pyqt_qstackedwidget.htm

        If the specified page has any objects that needs to be initialized
        then the process will be ran through here.

        Args => i => the int for the page wanted. Ranging from 0-3

        Return => None
        """
        self.ui.page_layer.setCurrentIndex(i)

        if(i == 0):
            print("starting VideoCapture")
            # creating a thread to update images when complete.
            # update images in gui
            update = UpdateImages(self.ui)
            # connect signal
            self.connect(update, QtCore.SIGNAL("update_images(PyQt_PyObject)"),
                         self.update_images)
            # intialize the video_capture object
            self.video_capture = VideoCapture(self.ui, update)
            # connect video_capture to main gui thread
            self.connect(self.video_capture,
                         QtCore.SIGNAL("update_capture(QImage)"),
                         self.update_capture)
            self.camera.start_video_capture(self.video_capture)

    def update_images(self, images):
        """
        Summary => update all images in the ui.

        Description => This method will be called, when any of the non-static
                images in the ui has been updated.

                Works by when a signal is called from another thread it will
                update the given images. That are sent through a list.

        Args => images - list - this is a list of string for the images
                                that want to be updated in this method.

        Return => None
        """
        pixmap = QtGui.QPixmap(images[0])
        pixmap = pixmap.scaled(498, 300, QtCore.Qt.KeepAspectRatio)
        self.ui.captured_image.setPixmap(pixmap)
        self.ui.captured_image.setAlignment(QtCore.Qt.AlignCenter)

        pixmap = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
        self.ui.image_your_picture.setPixmap(pixmap)

        pixmap = QtGui.QPixmap(images[1])
        pixmap = pixmap.scaled(498, 300, QtCore.Qt.KeepAspectRatio)
        self.ui.styled_image.setPixmap(pixmap)
        self.ui.styled_image.setAlignment(QtCore.Qt.AlignCenter)

    def update_capture(self, img):
        """
        Summary => update the capture image.

        Description => This method will be called, when the video_capture is
                    running.

                    Will update the video_capture img/Qlabel every time
                    a new image comes through.

        Args => None

        Return => None
        """
        pixmap = QtGui.QPixmap(img)
        pixmap = pixmap.scaled(498, 300, QtCore.Qt.KeepAspectRatio)
        self.ui.video_capture.setPixmap(pixmap)
        self.ui.video_capture.setAlignment(QtCore.Qt.AlignCenter)

# ------------------------------------------------------------
# Actions
# ------------------------------------------------------------

    def proccess_image(self):
        """
        Summary => starts the process for proccessing.

        Description => start the process for processing the image that
                was captured ealier on in the gui. This method will be
                a action used for the specified button.

        Args => None

        Return => None
        """
        print("Image processed")
        self.dithering = Dithering(self.ui, 10)
        self.dithering.run()
        # update images in gui
        update = UpdateImages(self.ui)
        # connect signal
        self.connect(update, QtCore.SIGNAL("update_images(PyQt_PyObject)"),
                     self.update_images)
        update.start()
        self.display_stack(3)

    def capture_image(self):
        """
        Summary => starts the process to capture the picture.

        Description => starts the process to capture the picture from the
                video feed. This image will be saved to 'Image/takenPicture'.

        Args => None

        Return => None
        """
        print("taken picture!!!!!")
        # stop the video feed from the camera, until enter the page again.
        self.camera.stop_video_capture()
        # sleep to let the program to update, before changing screen
        time.sleep(0.1)
        # changed to the acceptance page, after picture has been taken
        self.display_stack(1)

    def accept_picture(self):
        """
        Summary => action to take the user to the next page.

        Description => when this action is given, it will take the user to
                the style picking page.

        Args => None

        Return => None
        """
        self.display_stack(2)

    def start_plot(self):
        """
        Summary => Will initialize the plotting process.

        Description => will initialize the plotting process from the
                coordinates given, when the image has been changed in the
                styling stage.

        Args => None

        Return => None
        """
        print("plotting")
        # get coordinates
        coord = self.self.dithering.get_coordinates()
        # coord = self.image_proccessor.get_coordinates()
        # create the plotter conroller (coordinates , scale)
        plotter = DitheringPlotter(coord, 1)
        # call run, when ready to throw through the process.
        plotter.run()

    def reject_style(self):
        """
        Summary => will reject the current style and ask if they are sure.

        Description => will reject the current stlye and before returning
                to the previous stage. The program will ask if they are sure
                by using a message box.

        Args => None

        Return => None

        """
        # if no, display message box to make sure that they don't want the
        # the image
        choice = QMessageBox.question(self, 'Are you sure',
                                            "Are you sure that you do not want"
                                            + " this image, if not you will be"
                                            + " returned to styling page?",
                                            QMessageBox.Yes |
                                            QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.display_stack(2)
        else:
            pass

    def reject_picture(self):
        """
        Summary => will reject the current picture and ask if they are sure.

        Description => will reject the current picture and before returning
                to the previous stage. The program will ask if they are sure
                by using a message box.

        Args => None

        Return => None
        """
        # if no, display message box to make sure that they don't want the
        # the image
        choice = QMessageBox.question(self, 'Are you sure',
                                            "Are you sure that you do not want"
                                            + " this image, if not you will be"
                                            + " returned to home page?",
                                            QMessageBox.Yes |
                                            QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.display_stack(0)
        else:
            pass

    def close_application(self):
        """
        Summary => will close the Gui.

        Description => will create a message box that will ask if you
        want to leave the Application. If yes, Application is closed and if
        no - return to Application

        Args => None

        Return => None
        """
        # creating exit pop-up message
        choice = QMessageBox.question(self, 'Leaving Application',
                                            "Leave Application?",
                                            QMessageBox.Yes |
                                            QMessageBox.No)
        # do actions depending on response
        if choice == QMessageBox.Yes:
            # close the camera feed, if it is still running
            self.camera.stop_video_capture()
            # reset each of the images to blank, when closed
            cv2.imwrite("Images/takenPicture.jpg", cv2.imread(
                                                        "Images/blank.jpg"))
            cv2.imwrite("Images/proccessedImage.jpg", cv2.imread(
                                                        "Images/blank.jpg"))
            print("Leaving Application")
            sys.exit()
        else:
            pass
