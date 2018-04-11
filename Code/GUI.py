"""
Summary => Will be used to control and generate a GUI.

Description => This class will be used to generate and control the GUI used
for the system. You will be able to control the camera and see the feed
comming from it.

Author => Matthew Howard (mah60).
Version => 0.1 - 24/02/2018 -
"""
import sys
# from PyQt4 import QtGui, QtCore
from PyQt5.QtGui import QDialog
from ui_imagedialog import Ui_ImageDialog
import Robotic_Artist_GUI as main_window


class GUI(QtGui.QMainWindow):  # TODO: give a better name e.g. window, Gui is
                                # the whole Application
        """
        Summary => maintain the GUI used to control the robotic artist.

        Description =>
        """

        def __init__(self, ap):
            """
            Summary => Will create a GUI object.

            Description =>

            Args =>
            """
            super(GUI, self).__init__()
            self.app = ap
            self.window = QtWidgets.QMainWindow()

            window_view = main_window.Ui_mainWindow()
            window_view.setupUi(self.window)
            """
            self.resize(750, 500)
            self.move(150, 150)
            self.setWindowTitle('Robotic artist : Walter')
            # TODO: create a better Icon for the window
            self.setWindowIcon(QtGui.QIcon('Images/Icon.png'))

            # coding for the main menu
            # ---------------------------------
            # Actions
            # escape action, will exit the Application when activated
            escapeAction = QtGui.QAction('&Exit Application', self)
            escapeAction.setShortcut('Ctrl+Q')
            escapeAction.setStatusTip('Leaving Application')
            escapeAction.triggered.connect(self.close_application)
            # login action for admin
            adminLoginAction = QtGui.QAction('&Admin Login', self)
            adminLoginAction.setStatusTip('Logging into Admin')
            # TODO: create login for admin
            adminLoginAction.triggered.connect(self.close_application)
            # toggle admin view
            toggleAdminAction = QtGui.QAction('&Toggle Admin View', self)
            toggleAdminAction.setShortcut('Ctrl+A')
            toggleAdminAction.setStatusTip('Admin view open')
            toggleAdminAction.triggered.connect(self.close_application)
            # help action, to display the tutorial
            tutorialAction = QtGui.QAction('&Tutorial', self)
            tutorialAction.setShortcut('Ctrl+H')
            tutorialAction.setStatusTip('Admin view open')
            tutorialAction.triggered.connect(self.close_application)
            # creates a statusBar
            self.statusBar()

            # sets up the main menu. Can add actions to them here
            mainMenu = self.menuBar()
            # make file menu
            fileMenu = mainMenu.addMenu('&File')
            fileMenu.addAction(escapeAction)  # adds escapeAction to fileMenu
            # make admin menu
            adminMenu = mainMenu.addMenu('&Admin')
            # adds adminLoginAction and toggleAdminAction to adminMenu
            adminMenu.addAction(adminLoginAction)
            adminMenu.addAction(toggleAdminAction)
            # make help menu
            helpMenu = mainMenu.addMenu('&Help')
            # adds tutorialAction to helpMenu
            helpMenu.addAction(tutorialAction)
            # ---------------------------------

            self.main_window()

            sys.exit(self.app.exec_())
            """
# -----------------------------------------------------------
# views
# -----------------------------------------------------------

        def main_window(self):
            """
            Summary => Will create a GUI object.

            Description =>

            Args
            """
            # btn = QtGui.QPushButton("Capture", self)
            # this is a set of code that will caputre an image
            # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)

            # will call the capture_image function. Used to take a picture with
            # the camera
            # btn.clicked.connect(self.capture_image)

            # there are 3 methods to adjusting the size of the QPushButton
            # 1. standard input values x,y size.
            # 2. btn.resize(btn.sizeHint()) - will give most suggested size for
            # object according to other variables
            # 3. btn.resize(btn.minimumSizeHint()) - will give the smallest
            # size suggestion for the button
            # btn.resize(btn.sizeHint())
            # btn.move(50, 50)

            self.show()

        def photo_display(self):
            """
            Summary => Will create a GUI object.

            Description =>

            Args
            """

        def style_selection(self):
            """
            Summary => Will create a GUI object.

            Description =>

            Args
            """

        def admin_window(self):
            """
            Summary => Will create a GUI object.

            Description =>

            Args
            """

        def description_display(self):
            """
            Summary => Will create a GUI object.

            Description =>

            Args
            """

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

        def close_application(self):
            """
            Summary => Will create a GUI object.

            Description =>

            Args
            """
            # creating exit pop-up message
            choice = QtGui.QMessageBox.question(self, 'Leaving Application',
                                                "Leave Application?",
                                                QtGui.QMessageBox.Yes |
                                                QtGui.QMessageBox.No)
            # do actions depending on response
            if choice == QtGui.QMessageBox.Yes:
                print("Leaving Application")
                sys.exit()
            else:
                pass
