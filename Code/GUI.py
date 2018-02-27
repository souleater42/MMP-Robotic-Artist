"""
Summary => Will be used to control and generate a GUI.

Description => This class will be used to generate and control the GUI used
for the system. You will be able to control the camera and see the feed
comming from it.

Author => Matthew Howard (mah60).
Version => 0.1 - 24/02/2018 -
"""
import sys
from PyQt4 import QtGui


class GUI(object):
        """
        Summary => maintain the GUI used to control the robotic artist.

        Description =>
        """

        def __init__(self):
            """
            Summary => Will create a GUI object.

            Description =>

            Args =>
            """
            self.app = QtGui.QApplication(sys.argv)

            self.window = QtGui.QWidget()
            self.window.resize(750, 500)
            self.window.move(150, 150)
            self.window.setWindowTitle('Robotic artist : Walter')
            # TODO: create a better Icon for the window
            self.window.setWindowIcon(QtGui.QIcon('../Images/Icon.png'))
            self.window.show()

            sys.exit(self.app.exec_())
