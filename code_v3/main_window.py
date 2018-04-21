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
           0.4 - 20/04/2018 -  changed the image_proccesor and
                        plotter_controller to the dithering and
                        dithering_plotter as they are children of those
                        classes and will print out there specific style.
           0.4.1 - 21/04/2018 - changed proccess_image and start_plot.
                        to loop through every plotter and proccessor that
                        have been added to their arrays.

                        Updated the gui, so that the check boxes now work.
                        As well there is now a method restart_application
                        that is attached to the menubar so it can be
                        restart.
           0.4.2 - 21/04/2018 - removed ui as a args for the proccessors
                        as it is not used.

                        modified restart_application, so that you cannot
                        restart on first page avoiding error in camera.
"""
import time
import sys
import cv2
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMessageBox
from gui_view import Ui_mainWindow

from camera_controller import CameraController
from video_capture import VideoCapture
from update_images import UpdateImages

from dithering import Dithering
from edges_style import EdgesStyle

from dithering_plotter import DitheringPlotter
from edges_style_plotter import EdgeStylePlotter


class MainWindow(QtGui.QMainWindow):
    """
    Summary => maintain the GUI used to control the robotic artist.

    Description => This class will be used to generate and control the GUI used
    for the system. You will be able to control the camera and see the feed
    comming from it.

    args => None

    return => None
    """

    def __init__(self):
        """
        Summary => initialize the main window view.

        Description =>

        args => None

        return => None
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
        restart_application = QtGui.QAction("&Restart Application", self)
        restart_application.setShortcut("R")
        restart_application.setStatusTip('Leave The App')
        restart_application.triggered.connect(self.restart_application)
        self.ui.menuFile.addAction(restart_application)

        # set unworking menuBar items, to display error message
        self.ui.actionLogin.triggered.connect(
                                                        self.trigger_error)
        self.ui.actionToggle_Admin_View.triggered.connect(
                                                        self.trigger_error)
        self.ui.actionTutorial.triggered.connect(
                                                        self.trigger_error)

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

        # style check boxes
        self.style_check_boxes = [
                                 self.ui.check_style1,
                                 self.ui.check_style2,
                                 self.ui.check_style3,
                                 self.ui.check_style4,
                                 self.ui.check_style5
                                 ]
        # set styles labels
        self.style_check_boxes[0].setText("Dithering")
        self.style_check_boxes[1].setText("edges")
        self.style_check_boxes[2].setText("No Style")
        self.style_check_boxes[3].setText("No Style")
        self.style_check_boxes[4].setText("No Style")
        # set style images
        pixmap = QtGui.QPixmap('Images/dithering_example.jpg')
        self.ui.image_style1.setPixmap(pixmap)

        pixmap = QtGui.QPixmap('Images/edges_style_example.jpg')
        pixmap = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
        self.ui.image_style2.setPixmap(pixmap)

        pixmap = QtGui.QPixmap("Images/blank_image.jpg")
        self.ui.image_style3.setPixmap(pixmap)

        pixmap = QtGui.QPixmap("Images/blank_image.jpg")
        self.ui.image_style4.setPixmap(pixmap)

        pixmap = QtGui.QPixmap("Images/blank_image.jpg")
        self.ui.image_style5.setPixmap(pixmap)

        # import text for description
        # got technique from
        # https://stackoverflow.com/questions/8369219/
        # how-do-i-read-a-text-file-into-a-string-variable-in-python
        text = ""
        with open('description.txt', 'r') as myfile:
            text = myfile.read()
        # set discription text
        self.ui.description_text.setText(text)
# ------------------------------------------------------------
# methods
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

        args => i => the int for the page wanted. Ranging from 0-3

        return => None
        """
        self.ui.page_layer.setCurrentIndex(i)

        if(i == 0):
            print("starting VideoCapture")
            # set checked_boxes to false
            self.ui.check_process.setChecked(False)
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
        elif(i == 2):
            # set check boxes to false
            for check in self.style_check_boxes:
                check.setChecked(False)

    def update_images(self, images):
        """
        Summary => update all images in the ui.

        Description => This method will be called, when any of the non-static
                images in the ui has been updated.

                Works by when a signal is called from another thread it will
                update the given images. That are sent through a list.

        args => images - list - this is a list of string for the images

        return => None
        """
        pixmap = QtGui.QPixmap(images[0])
        # update images throughout gui that are not static.
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

        args => None

        return => None
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

        args => None

        return => None
        """
        print("Image processing")
        self.proccessors = [
                            Dithering(),
                            EdgesStyle()
                            ]
        no_check = True
        checked = 0
        # loop through every proccessor
        for i, proccessor in enumerate(self.proccessors):
            # check if check_box style has been ticked
            if self.style_check_boxes[i].isChecked():
                # run the processor
                proccessor.run()
                no_check = False
                checked = checked + 1
        # check if no check_boxs have been ticked
        if no_check:
            error = QMessageBox()
            error.setIcon(QMessageBox.Information)
            error.setText("No style selected \n Please select the syle wanted")
            error.setWindowTitle("Error: No style")
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        else:
            if checked == 1:
                # update images in gui
                update = UpdateImages(self.ui)
                # connect signal to update thread
                self.connect(update, QtCore.SIGNAL(
                             "update_images(PyQt_PyObject)"),
                             self.update_images)
                # run the update thread
                update.start()

                # display the next page
                self.display_stack(3)
            else:
                error = QMessageBox()
                error.setIcon(QMessageBox.Information)
                error.setWindowTitle("Error: Too many styles")
                error.setText("Too many style selected \n Please pick one")
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()

    def capture_image(self):
        """
        Summary => starts the process to capture the picture.

        Description => starts the process to capture the picture from the
                video feed. This image will be saved to 'Image/takenPicture'.

        args => None

        return => None
        """
        print("taken picture!!!!!")
        if self.ui.check_process.isChecked():
            # sleep to let the program to update, before changing screen
            time.sleep(0.1)
            self.camera.stop_video_capture()
            # changed to the acceptance page, after picture has been taken
            self.display_stack(1)
        else:
            error = QMessageBox()
            error.setIcon(QMessageBox.Information)
            error.setText("Please confirm that we can process your pitcture")
            error.setWindowTitle("Confirmation")
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    def accept_picture(self):
        """
        Summary => action to take the user to the next page.

        Description => when this action is given, it will take the user to
                the style picking page.

        args => None

        return => None
        """
        self.display_stack(2)

    def start_plot(self):
        """
        Summary => Will initialize the plotting process.

        Description => will initialize the plotting process from the
                coordinates given, when the image has been changed in the
                styling stage.

        args => None

        return => None
        """
        print("plotting")
        # create the plotter conroller (coordinates , scale)
        # plot coords for dithering style
        self.plotters = [
                        DitheringPlotter(
                                        self.proccessors[1].get_coordinates(),
                                        1),
                        EdgeStylePlotter(
                                        self.proccessors[2].get_coordinates()
                                        , 1)
                        ]
        # call run, when ready to throw through the process.
        for plotter, i in enumerate(self.plotters):
            # need to check if thread is running, so doesn't start more
            # than one thread from pressing button muiltiple times.
            if not plotter.is_alive():
                # check if specified style is ticked
                if self.style_check_boxes[i].isChecked():
                    plotter.start()

    def reject_style(self):
        """
        Summary => will reject the current style and ask if they are sure.

        Description => will reject the current stlye and before returning
                to the previous stage. The program will ask if they are sure
                by using a message box.

        args => None

        return => None

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

        args => None

        return => None
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

        args => None

        return => None
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

    def restart_application(self):
        """
        Summary => will restart the Gui.

        Description => will create a message box that will ask if you
        want to restart the Application. If yes, Application will restart and
        set back to the first page and if no - return to Application.

        args => None

        return => None
        """
        if self.ui.page_layer.currentIndex() == 0:
            error = QMessageBox()
            error.setIcon(QMessageBox.Information)
            error.setText("Cannot restart this page")
            error.setWindowTitle("Error: cannot restart")
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        else:
            # creating exit pop-up message
            choice = QMessageBox.question(self, 'Restarting Application',
                                                "Restart Application?",
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
                print("Restarting Application")
                # change bk to front page
                self.display_stack(0)
            else:
                pass

    def trigger_error(self):
        """
        Summary => will send out of order error.

        Description => will send out of order error message.
                This message is to say that this part of the program is
                either broken or not complete.

        args => None

        return => None
        """
        error = QMessageBox()
        error.setIcon(QMessageBox.Information)
        error.setText("Error: this function is currently out of use")
        error.setWindowTitle("Error: Out of order")
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()
