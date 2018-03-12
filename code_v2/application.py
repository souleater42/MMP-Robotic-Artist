import sys
# from PyQt5.QtWidgets import QApplication, QDialog
from main_window import MainWindow
# from serial_control import SerialControl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    # ui = Ui_mainWindow()
    # ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
