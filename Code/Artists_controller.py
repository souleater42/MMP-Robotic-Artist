"""
Summary => The controller class for the Robotic aritst.

Description => TODO: add a description.

Author => Matthew Howard (mah60).
Version => 0.1 - 23/02/2018 - This version is the intial set up for the
controller. It contains a basic initialization setup and a way to read any
input.
"""
import serial


def read_all():
    """
    Summary => Will be used to read all incoming data from the serial.

    Description => Will be used to read all incoming input from the serail. If
    there is no input from the serial the session will time out and return
    to the normal process.
    """
    buffer = ""
    # check if there are any expected input from the serial
    while ser.in_waiting:
        # if there is incomming input, throw into loop and
        # read the loop
        char = ser.read()
        # turn byte into ascii
        char = char.decode("utf-8")
        # when '\r' appears end reading process
        if char == '\r':
            break
        else:
            # add to buffer
            # print(char)
            buffer += char
    return buffer


if __name__ == "__main__":
    # setup serial import
    # TODO :create method to check for other ports
    ser = serial.Serial('/dev/ttyUSB0', 9600, stopbits=1, parity='E')

    ser.write(b'OC;')
    print('OC')
    print(read_all())
