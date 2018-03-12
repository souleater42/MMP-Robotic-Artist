"""
Summary => Will be used to control and generate a GUI.

Description => This class will be used to generate and control the GUI used
for the system. You will be able to control the camera and see the feed
comming from it.

Author => Matthew Howard (mah60).
Version => 0.1 - 12/03/2018 -
"""
import sys
from gui_view import Ui_mainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindow(QtWidgets.QMainWindow):
    """
    Summary => maintain the GUI used to control the robotic artist.

    Description =>
    """

    def __init__(self):
        """
        Summary => initialize the main window view.

        Description =>
        """
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.move(100, 100)  # move gui to the 100,100 on the screen
        self.setWindowIcon(QtGui.QIcon('Images/Icon.png'))  # sets icon for gui
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
        #self.ui.yes_no_button.clicked.connect(self.accept_picture)

# ------------------------------------------------------------
# functions
# ------------------------------------------------------------

    def display_stack(self, i):
        """
        Summary => Will create a GUI object.

        Description => will change th stacked widget view to the int given
        through i.

        This code was found on:
        https://www.tutorialspoint.com/pyqt/pyqt_qstackedwidget.htm

        Args -> i -> the int for the page wanted. Ranging from 0-3
        """
        self.ui.page_layer.setCurrentIndex(i)
# ------------------------------------------------------------
# Actions
# ------------------------------------------------------------

    def capture_image(self):
        """
        Summary => Will create a GUI object.

        Description =>

        Args
        """
        print("taken picture!!!!!")
        self.display_stack(1)

    def accept_picture(self):
        """
        Summary => Will create a GUI object.

        Description =>

        Args
        """
        self.display_stack(2)

    def reject_picture(self):
        """
        Summary => Will create a GUI object.

        Description =>

        Args
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

        Args - None
        return - None
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
