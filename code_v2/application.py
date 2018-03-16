"""
Summary => The controller class for initializing the Robotic aritst.

Description => TODO: add a description.

Author => Matthew Howard (mah60).
Version =>
0.1 - 23/02/2018 - This version is the intial set up for the
controller. It contains a basic initialization setup and a way to read any
input.
0.1.1 - 26/02/2018 - corrected the calling of the serial command.
0.2 - 12/03/2018 - recreated file and renamed it to Application.py. This code
is now in code_v2. The basic set has done to start the gui and run the program
as a whole.
"""
import sys
from main_window import MainWindow
from PyQt5.QtWidgets import QApplication


def main():
    """
    Summary => will initilize the robotic artist.

    Description =>

    args => None

    None => None
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    # ui = Ui_mainWindow()
    # ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
