"""
Summary => used to control the input and output to that serial port.

Description => This class will be used to initialize and control the serial.
There are methods to read and send messages to the serial given to it.

Author => Matthew Howard (mah60).
Version =>
0.1 - 23/02/2018 - intial set up for the class, this will be
initialization of the serial connection at creation of serial. As well,
functions to read and write to serial connection.
0.1.1 - 26/02/2018 -  made some print commands to print input and output
from the serial connection.
"""
import serial
from time import sleep


class serial_control(object):
    """
    Summary => used to control the input and output to that serial port.

    Description => Will be used to control the serial port and send input
        and outputs to the serial given to the object. This object will store
        the serial connection link as 'ser'. Also, will store all serial ports
        values as variables.
    """

    def __init__(self, sp, b='9600', sb=1, p='E'):
        """
        Summary => Will initialize serial port and make a connection to it.

        Description => creates an object to create and control a serial
        connection. The serial_port, stopbits, baund and parity will be stored
        to access later. Will initialize the serial as ser.

        Args =>
            sp = serial_port = serial port that you wish to connet to
            sb = stopbits = the amount of stopbits you want. default = 1
            b = baund = the baund speed. default = '9600'
            p = parity = the parity of the serial. default = 'E'
        """
        self.serial_port = sp
        self.stopbits = sb
        self.baund = b
        self.parity = p
        self.ser = serial.Serial(self.serial_port, self.baund,
                                 stopbits=self.stopbits, parity=self.parity)

    
    def read_all(self):
        """
        Summary => handle all messages being recieved from serial connection.

        Description => Will be used to read all incoming input from the serail.
        If there is no input from the serial the session will time out and
        return to the normal process.

        return => null if no response or the string of input from incoming
            message
        """
        buffer = ""
        # check if there are any expected input from the serial
        while self.ser.in_waiting:
            # if there is incomming input, throw into loop and
            # read the loop
            char = self.ser.read()
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

    def write(self, command):
        """
        Summary => handles all messages being sent to the serial.

        Description => Will write to the serial given to this class and then
            will read from the serial to see if there is a returned message.
            If not will return none.

        arguments =>
            command => this will be a string of the command you want
                to send to the serial, connected to this object.
        return => string, if there is any response from called command. If not
            the response will be None
        """
        # writes to the serial and converts message to bytes
        self.ser.write(command.encode('utf-8'))
        # will make the program sleep for 100 ms to see if there is a response
        sleep(0.5)
        # returns a response if one exists
        print(command)
        response = self.read_all()
        print(response + "-----")
        return response
