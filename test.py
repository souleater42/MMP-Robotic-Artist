import serial
'''
def set_serial():
    ser = serial.Serial('dev/ttyUSB0', 9600, stopbits=1, parity='E')
    if check_serial(ser):
        return ser
    else:
        return serial.Serial('dev/ttyUSB1', 9600, stopbits=1, parity='E')

def check_serial(ser):
    ser.write('OC;')
    fin = 0
    while(fin == 0):
        char = ser.read();
        if char == '\r':
            fin = 1
            return true
        else:
            print(char)
'''


if __name__ == "__main__":
    #sets up the serial port, to be able to communicate with the plotter
    #ser = set_serial()
    ser = serial.Serial('dev/ttyUSB0', 9600, stopbits=1, parity='E')
    ser.write('PA 400 400;')
    ser.write('PA 2000 2000;')
    ser.write('PA 5000 500;')
    ser.write('PA 6000 400;')
    ser.write('PA 0 0;')
