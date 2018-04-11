"""
Summary => Will be used to control and generate a GUI.

Description => This class will be used to generate and control the GUI used
for the system. You will be able to control the camera and see the feed
comming from it.

Author => Matthew Howard (mah60).
Version => 0.1 - 24/02/2018 -
"""
from PyQt5.QtGui import QDialog
from ui_imagedialog import Ui_ImageDialog
import Robotic_Artist_GUI as main_window

class Window(QtGui.QMainWindow):
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
            super(ImageDialog, self).__init__()
            
