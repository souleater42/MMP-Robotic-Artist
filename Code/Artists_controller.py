"""
Summary => The controller class for the Robotic aritst.

Description => TODO: add a description.

Author => Matthew Howard (mah60).
Version =>
0.1 - 23/02/2018 - This version is the intial set up for the
controller. It contains a basic initialization setup and a way to read any
input.
0.1.1 - 26/02/2018 - corrected the calling of the serial command.
"""
import serial_control as ser
import GUI
#import Robotic_Artist_GUI

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
    

if __name__ == "__main__":

    # setup serial import
    ser = ser.serial_control("/dev/ttyUSB0")
    # ser = serial.Serial('/dev/ttyUSB0', 9600, stopbits=1, parity='E')
    #ser.write('PA 5000 5000;')
    #ser.write('RR 40 40;')

    draw_hi(ser)

    #Gui = GUI.GUI()
