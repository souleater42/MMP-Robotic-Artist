"""
Summary => will control the pen plotter.

Description => will control the pen plotter and print off the x and y
        coordinates given to it at run time. This object when run will go
        through a drawing out all the coordinates and making connections
        between each point. Then draw those lines out.

        When you want to start the process, call the method run().
        Then this method will go through the process of printing out the
        given coordinates.

Author => Matthew Howard (mah60).
Version => 0.1 - 15/03/2018 - This is the basic set up to this class.
                it has been designed to take coordinates and scale When
                first drawn. Then will proccess the coordinates to the plotter
                when the method run() is called.

                The methods run(), draw(), check_move(), connections(),
                move(), coordinate_to_plotter(), test_coords() have been made.
           0.2 - 15/04/2018 - update change code to support python2 instead
                of python3. No changes made.
           0.3 - 20/04/2018 - moving code to do with plotting coordinate for
                edges stlye to its own class. That inherits this one. This
                is because the methods moved are not gerneric to all the
                plotter_controllers.

                The methods moved are;
                    run(), draw(), check_move(), connection(), move()

                Created a run() message for this thread. Saying you are running
                the wrong thread.

                Created time_start and time_stop methods to time how long
                a plot will take.

"""
from xy_coordinate import XYCoordinate
from serial_control import SerialControl as serial
from threading import current_thread
import threading
import time
import numpy as np


class PlotterController(threading.Thread):
    """
    Summary => will control the proccess to plot out the coordinates given.

    Description => will process the coordinates given to it and print out those
            coordinates on the pen plotter when run() is called.

            This will make connections between each coordinate and draw
            lines between them.

    args => coordinates - list - a list of xy coordinates.
            scale - float - this will be the scale of which you want to be
                    drawn at. e.g. half the size will be 2 and double the
                    size will be 0.5

    return => None
    """
    
    

    def __init__(self, coordinates, scale):
        """
        Summary => initialize the PlotterController.

        Description => will create the plotter controller. Will take and input
            of coordinates and place them into a list until the method run()
            is called. To start the process.

        args => coordinates - list - a list of xy coordinates
                scale - float - this will be the scale of which you want to be
                        drawn at. e.g. half the size will be 2 and double the
                        size will be 0.5

        return => None
        """
        self.parent = current_thread()
        threading.Thread.__init__(self)
        
        self.ser = serial("/dev/ttyUSB0")
        self.coordinates = coordinates
        self.scale = scale

    def run(self):
        """
        Summary => running a blank thread.

        Description => will print error message. As they are running a black
                thread.

        args => None

        return => None
        """
        print("-------------------------------------------------------")
        print("error: plotter thread is empty.")
        print("       Advice:")
        print("              plotter is wrong type.")
        print("-------------------------------------------------------")

    def coordinate_to_plotter(self, xy_value):
        """
        Summary => will translate coordinates to plotter values.

        Description => will translate coordinates to plotter values. Which
            is fourty times the coordinate value for one point.

            The final value will be devided by the scale. Making it so
            the final result can be scaled up or down.

        args => xy_value - int - the curret coordinate value, that wants to
                    be translated to plotter values.

        return => int - the plotter value, that has been scaled.
        """
        return round(((xy_value * 40)/self.scale))

    def time_start(self):
        """
        Summary => starts timer on plotter.

        Description => starts timer on plotter.

        args => None

        return => None
        """
        self.start = time.time()

    def time_stop(self):
        """
        Summary => stops timer on plotter.

        Description => stops timer on plotter and prints out final
                result on plotter though hours.

        args => None

        return => None
        """
        # get end plot time
        self.end = time.time()
        # get the amount of seconds the plotter has been going for
        seconds = self.end - self.start
        minutes = seconds / 60
        hours = minutes / 60
        # This is the amound of time the plotter took to print.
        print("-------------------------------------------------------")
        print("hours : {0:.2f}".format(hours))
        print("-------------------------------------------------------")

    def test_coords(self):
        """
        Summary => generates test values for the coordinates.

        Description => will create test values for the coordinates. To
        be sent through the plotting stages.

        args => None

        return => None
        """
        self.coordinates = np.zeros(16, dtype=XYCoordinate)
        self.coordinates[0] = XYCoordinate(1, 1)
        self.coordinates[1] = XYCoordinate(1, 10)
        self.coordinates[2] = XYCoordinate(1, 2)
        self.coordinates[3] = XYCoordinate(1, 3)
        self.coordinates[4] = XYCoordinate(1, 4)
        self.coordinates[5] = XYCoordinate(1, 5)
        self.coordinates[6] = XYCoordinate(1, 6)
        self.coordinates[7] = XYCoordinate(2, 4)
        self.coordinates[8] = XYCoordinate(3, 4)
        self.coordinates[9] = XYCoordinate(4, 5)
        self.coordinates[10] = XYCoordinate(5, 6)
        self.coordinates[11] = XYCoordinate(7, 1)
        self.coordinates[12] = XYCoordinate(7, 2)
        self.coordinates[13] = XYCoordinate(7, 3)
        self.coordinates[14] = XYCoordinate(7, 5)
        self.coordinates[15] = XYCoordinate(8, 8)
