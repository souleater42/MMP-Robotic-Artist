"""
Summary => will plot the coordinates for the dithering alogorithm.

Description => will plot the coordinates for the edges style. This will
        involve plotting coordinates together that are next each other.

Author => Matthew Howard (mah60).
Version =>   0.1 - 20/04/2018 - created the basic layout from the code
                moved from the plotter_controller module.

                Check plotter_controller version, for older versions of
                the code.
"""
from __future__ import division
from xy_coordinate import XYCoordinate
from serial_control import SerialControl as serial
from plotter_controller import PlotterController
import time


class EdgeStylePlotter(PlotterController):
    """
    Summary => will plot the coordinates for the dithering alogorithm.

    Description => will plot the coordinates for the edges style. This will
            involve plotting coordinates together that are next each other.

    args => None

    return => None
    """

    def __init__(self, coordinates, scale):
        """
        Summary => will initialize the dithering plotter.

        Description => will initialize the DitheringPlotter, this will
                be used later to plot objects.

        args => coordinates -> numpy array - this is a array of XYCoordinates
                                that are wanting to be plotted.
                scale -> int - this is the scale of the final plot in
                            comparison to the coordinates.
                                coordinates/scale
        return => None
        """
        super(EdgeStylePlotter, self).__init__(coordinates, scale)

    def run(self):
        """
        Summary => run the PlotterController.

        Description => will run the plotter controller, this will take the
            coordinates given and turn them into lines. Using a linked-list
            format.

            After the lines have been made it will print out the list of lines


        args => None

        return => None
        """
        # if self.coordinates is None:
        #    self.test_coords()  # generate a bunch of test_coords
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

        args => None

        return => None
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

        args => point - XYCoordinate - this is the current location
                        coordinates.
                x - int - the x location of the current coordinate translated
                        to the plotters coordinates.
                        # check North
                y - int - the y location of the current coordinate translated
                        to the plotters coordinates.

        return => None
        """
        for move_to in self.coordinates:
            # check if it is the same location as current point
            if point != move_to:
                # check if move_to has already been drawn
                if not move_to.is_plotted():
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

        args => point - XYCoordinate - this is the current location
                        coordinates.
                move_to - XYCoordinate - this is the location of the
                        point that we may be moving to. If the test is
                        passed
                x_modifier - int - the modifier to the x plane, to compare if
                        it can move to given area.
                y_modifier - int -  the modifier to the y plane, to compare if
                        it can move to given area.

        return => True if the two points match, when the current location is
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

        args => point - XYCoordinate - this is the current location
                        coordinates.
                move_to - XYCoordinate - this is the new location
                                coordinates.
                x - int - the x location of the current coordinate translated
                        to the plotters coordinates.
                y - int - the y location of the current coordinate translated
                        to the plotters coordinates.

        return => int - the plotter value, that has been scaled.
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
