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
"""
from xy_coordinate import XYCoordinate
from serial_control import SerialControl as serial
import numpy as np


class PlotterController(object):
    """
    Summary => will control the proccess to plot out the coordinates given.

    Description => will process the coordinates given to it and print out those
            coordinates on the pen plotter when run() is called.

            This will make connections between each coordinate and draw
            lines between them.

    Args => coordinates - list - a list of xy coordinates.
            scale - float - this will be the scale of which you want to be
                    drawn at. e.g. half the size will be 2 and double the
                    size will be 0.5

    Return => None
    """

    def __init__(self, coordinates, scale):
        """
        Summary => initialize the PlotterController.

        Description => will create the plotter controller. Will take and input
            of coordinates and place them into a list until the method run()
            is called. To start the process.

        Args => coordinates - list - a list of xy coordinates
                scale - float - this will be the scale of which you want to be
                        drawn at. e.g. half the size will be 2 and double the
                        size will be 0.5

        Return => None
        """
        self.ser = serial("/dev/ttyUSB0")
        for x in coordinates:
            print(x)
        self.coordinates = coordinates
        self.scale = scale

    def run(self):
        """
        Summary => run the PlotterController.

        Description => will run the plotter controller, this will take the
            coordinates given and turn them into lines. Using a linked-list
            format.

            After the lines have been made it will print out the list of lines


        Args => None

        Return => None
        """
        if self.coordinates is None:
            self.test_coords()  # generate a bunch of test_coords
        self.draw()

    def draw(self):
        """
        Summary => draw the list of coordinates.

        Description => will loop through the list of coordinates given. Then
            will move to the given point and put the pen down. The method will
            proceed to find all connections to that point and draw to the new
            location. Then will return to the current location.

            After complete each coordinate value will be set to drawn,
            when then have been checked. So the program does not return to
            that location when drawing the other locations.

        Args => None

        Return => None
        """
        # select pen 1
        self.ser.write('SP 1;')
        for point in self.coordinates:
            # place pen at this points location
            x = self.coordinate_to_plotter(point.get_x())
            y = self.coordinate_to_plotter(point.get_y())
            str_command = "PA {} {};".format(x, y)
            self.ser.write(str_command)
            # put pen down
            self.ser.write('PD;')

            # check if there is a connection in each direction,
            # think of it like a compass North, North-East etc.
            self.check_move(point, x, y)
            # mark this point as drawn
            point.plotted()
            # at end bring pen back up
            self.ser.write("PU;")
        # select pen 0, disengage pen
        self.ser.write('SP 0;')

    def check_move(self, point, x, y):
        """
        Summary => check where the plotter can move to.

        Description => will check in all directions, north, west, north-West
            etc. To see where the pen can move_to following the constraits of
            other coordinates to this one.

            If the location has a connection to another point it will draw
            to that point and then return.

            Will check first if that point has already been drawn out to
            reduce the amount of cross overs.

        Args => point - XYCoordinate - this is the current location
                        coordinates.
                x - int - the x location of the current coordinate translated
                        to the plotters coordinates.
                y - int - the y location of the current coordinate translated
                        to the plotters coordinates.

        Return => None
        """
        for move_to in self.coordinates:
            # check if it is the same location as current point
            if point != move_to:
                # check if move_to has already been drawn
                if not move_to.is_plotted():
                    # check North
                    if self.connection(point, move_to, 0, 1):
                        self.move(point, move_to, x, y)
                    # check North-East
                    if self.connection(point, move_to, 1, 1):
                        self.move(point, move_to, x, y)
                    # check East
                    if self.connection(point, move_to, 1, 0):
                        self.move(point, move_to, x, y)
                    # check South-East
                    if self.connection(point, move_to, 1, -1):
                        self.move(point, move_to, x, y)
                    # check South
                    if self.connection(point, move_to, 0, -1):
                        self.move(point, move_to, x, y)
                    # check South-West
                    if self.connection(point, move_to, -1, -1):
                        self.move(point, move_to, x, y)
                    # check West
                    if self.connection(point, move_to, -1, 0):
                        self.move(point, move_to, x, y)
                    # check North-West
                    if self.connection(point, move_to, -1, 1):
                        self.move(point, move_to, x, y)

    def connection(self, point, move_to, x_modifier, y_modifier):
        """
        Summary => check if there is a connection between two points.

        Description => will check if there is a connection between two points,
            using a the x and y x_modifier to the current location of the pen.

            This will check if they are within the distance of connection of
            each other. To be able to connect to each other.

        Args => point - XYCoordinate - this is the current location
                        coordinates.
                move_to - XYCoordinate - this is the location of the
                        point that we may be moving to. If the test is
                        passed
                x_modifier - int - the modifier to the x plane, to compare if
                        it can move to given area.
                y_modifier - int -  the modifier to the y plane, to compare if
                        it can move to given area.

        Return => True if the two points match, when the current location is
                    modifed.
        """
        # check if both the y and x location are the same to the move_to point
        if ((point.get_x() + x_modifier) == move_to.get_x()) and (
                    (point.get_y() + y_modifier) == move_to.get_y()):
            # if they are the same when modifed return true
            return True
        else:
            # if they are not the same when modifed return false
            return False

    def move(self, point, move_to, x, y):
        """
        Summary => move to the new location and returns to point.

        Description => will move_to the new location given. After
                this the pen will be brought up and returns back to the
                current location point.

        Args => point - XYCoordinate - this is the current location
                        coordinates.
                move_to - XYCoordinate - this is the new location
                                coordinates.
                x - int - the x location of the current coordinate translated
                        to the plotters coordinates.
                y - int - the y location of the current coordinate translated
                        to the plotters coordinates.

        Return => int - the plotter value, that has been scaled.
        """
        # move pen to new found location, then return to current
        # point location
        str_command = "PA {} {};".format(self.coordinate_to_plotter(
                                      move_to.get_x()),
                                      self.coordinate_to_plotter(
                                      move_to.get_y()))
        self.ser.write(str_command)
        # pull pen up
        self.ser.write("PU;")
        # return to current location
        str_command = "PA {} {};".format(x, y)
        self.ser.write(str_command)
        # put pen down at returned point
        self.ser.write("PD;")

    def coordinate_to_plotter(self, xy_value):
        """
        Summary => will translate coordinates to plotter values.

        Description => will translate coordinates to plotter values. Which
            is fourty times the coordinate value for one point.

            The final value will be devided by the scale. Making it so
            the final result can be scaled up or down.

        Args => xy_value - int - the curret coordinate value, that wants to
                    be translated to plotter values.

        Return => int - the plotter value, that has been scaled.
        """
        return round(((xy_value * 40)/self.scale))

    def test_coords(self):
        """
        Summary => generates test values for the coordinates.

        Description => will create test values for the coordinates. To
        be sent through the plotting stages.

        Args => None

        Return => None
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
