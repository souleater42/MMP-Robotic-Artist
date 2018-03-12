import sys
# from PyQt5.QtWidgets import QApplication, QDialog
from main_window import MainWindow
from serial_control import SerialControl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def draw_hi(ser):

    ser.write('SP 1;')
    ser.write('PA 100 100;')
    ser.write('PD;')
    ser.write('PA 100 1000;')
    ser.write('PU;')

    ser.write('PA 100 550;')
    ser.write('PD;')
    ser.write('PA 550 550;')
    ser.write('PU;')

    ser.write('PA 550 100;')
    ser.write('PD;')
    ser.write('PA 550 1000;')
    ser.write('PU;')

    ser.write('PA 700 100;')
    ser.write('PD;')
    ser.write('PA 700 800;')
    ser.write('PU;')

    ser.write('PA 700 900;')
    ser.write('PD;')
    ser.write('PA 700 1000;')
    ser.write('PU;')

    ser.write('SP 0;')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    #ui = Ui_mainWindow()
    #ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
