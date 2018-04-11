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
"""
import sys
#from camera_controller import CameraController
#from image_proccesor import ImageProccesor
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
# QApplication, QMainWindow,
from gui_view import Ui_mainWindow
from plotter_controller import PlotterController
from update_images import UpdateImages
import time
#import cv2


class MainWindow(QtWidgets.QMainWindow):
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
        #self.camera = CameraController(self.ui, self.update_images)
        #self.image_proccessor = ImageProccesor(self.ui)
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
            #self.camera.start_video_capture()

    def update_images(self):
        """
        Summary => update all images in the ui.

        Description => This method will be called, when any of the non-static
                images in the ui has been updated.

        Args => None

        Return => None
        """


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
        #self.image_proccessor.boarders()
        # update images in gui
        update = UpdateImages(self.ui)
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
        #self.camera.stop_video_capture()

        # sleep to let the program to update, before changing screen
        time.sleep(5/60)

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
        #coord = self.image_proccessor.get_coordinates()
        # create the plotter conroller (coordinates , scale)
        self.plotter = PlotterController(None, 1)
        # call run, when ready to throw through the process.
        self.plotter.run()

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
           # self.camera.stop_video_capture()
            # reset each of the images to blank, when closed
            cv2.imwrite("Images/takenPicture.jpg", cv2.imread(
                                                        "Images/blank.jpg"))
            cv2.imwrite("Images/proccessedImage.jpg", cv2.imread(
                                                        "Images/blank.jpg"))
            print("Leaving Application")
            sys.exit()
        else:
            pass
