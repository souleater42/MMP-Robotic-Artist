"""
Summary => Will be used to control and generate a GUI.

Description => This class will be used to generate and control the GUI used
for the system. You will be able to control the camera and see the feed
comming from it.

Author => Matthew Howard (mah60).
Version => 0.1 - 12/03/2018 - has the basic set up for the gui. Created Actions
to control the transactions in the gui and the class is able to draw the gui
design from gui_view made in qt designer.
"""
import sys
# from camera_controller import CameraController
# from image_proccesor import ImageProccesor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
# QApplication, QMainWindow,
from gui_view import Ui_mainWindow
# from plotter_controller import PlotterController


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
        # self.camera = CameraController()
        # self.image_proccessor = ImageProccesor()
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
        pixmap = QtGui.QPixmap('Images/takenPicture.bmp')
        pixmap = pixmap.scaled(498, 300, QtCore.Qt.KeepAspectRatio)
        self.ui.captured_image.setPixmap(pixmap)
        self.ui.captured_image.show()
        self.ui.captured_image.setAlignment(QtCore.Qt.AlignCenter)
        pixmap = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
        self.ui.image_your_picture.setPixmap(pixmap)
        self.ui.image_your_picture.show()
        self.ui.btn_continue1.clicked.connect(self.proccess_image)
        pixmap = QtGui.QPixmap('Images/proccessed_image.bmp')
        pixmap = pixmap.scaled(498, 300, QtCore.Qt.KeepAspectRatio)
        self.ui.styled_image.setPixmap(pixmap)
        self.ui.styled_image.setAlignment(QtCore.Qt.AlignCenter)
        btn = self.ui.yes_no_button2.button(self.ui.yes_no_button.Yes)
        btn.clicked.connect(self.start_plot)
        btn = self.ui.yes_no_button2.button(self.ui.yes_no_button.No)
        btn.clicked.connect(self.reject_style)
        # pixmap = QtGui.QPixmap("Images/cap.jpg")
        # pixmap = pixmap.scaled(498, 300, QtCore.Qt.KeepAspectRatio)
        # self.ui.video_capture.setPixmap(pixmap)
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
            # self.camera.start_video_capture(12)
            # self.ui.captured_image.
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
        # self.image_proccessor.canny_style()
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
        # changed to the acceptance page, after picture has been taken
        self.display_stack(1)
        # stop the video feed from the camera, until enter the page again.
        # self.camera.stop_video_capture()

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
        # create the plotter conroller (coordinates , scale)
        # self.plotter = PlotterController(None, 1)
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
            print("Leaving Application")
            sys.exit()
        else:
            pass