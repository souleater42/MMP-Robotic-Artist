import serial

def read_all():

    buffer = ""
    while True:
        char = ser.read()
        if char == '\r':
            break
        else:
            buffer += char.decode("utf-8")
    return buffer


if __name__ == "__main__":

    ser = serial.Serial('/dev/ttyUSB0', 9600, stopbits=1, parity='E')

    ser.write(b'OC;')
    print(read_all())
