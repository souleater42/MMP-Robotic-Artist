"""
Summary => The controller class for the Robotic aritst.

Description => TODO: add a description.

Author => Matthew Howard (mah60).
Version => 0.1 - 23/02/2018 - This version is the intial set up for the
controller. It contains a basic initialization setup and a way to read any
input.
"""
import serial_control
import GUI

if __name__ == "__main__":
    # setup serial import
    ser = serial_control('/dev/ttyUSB0')
    # ser = serial.Serial('/dev/ttyUSB0', 9600, stopbits=1, parity='E')
    ser.write('OC;')
    print(ser.read_all())
