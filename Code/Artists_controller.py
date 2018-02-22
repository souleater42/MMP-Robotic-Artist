import serial

def read_all():

    buffer = ""
    while ser.in_waiting:
        char = ser.read()
        char = char.decode("utf-8")
        if char == '\r':
            break
        else:
            print(char)
            buffer += char
    return buffer


if __name__ == "__main__":

    ser = serial.Serial('/dev/ttyUSB0', 9600, stopbits=1, parity='E')

    ser.write(b'OC;')
    print('OC')
    print(read_all())
