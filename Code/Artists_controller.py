import serial

if __name__ == "__main__":

    ser = serial.Serial('dev/ttyUSB0', 9600, stopbits=1, parity='E')

    ser.write('PA 500 500;')
    ser.write('PA 5000 5000;')
    ser.write('PA 500 500;')
    ser.write('PA 5000 5000;')
    ser.write('PA 500 500;')
    ser.write('PA 5000 5000;')
    ser.write('PA 500 500;')
    ser.write('PA 5000 5000;')
