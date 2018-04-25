"""
Summary => will plot the coordinates for the dithering alogorithm.

Description => will plot the coordinates for the dithering alogorithm style.
            This will be done by sending commands to the plotter. This
            includes the command for HPGL such as;

                PA x y; - this will move the pen to that coordinate
                PU; - put the plotter pen into up position.
                PD; - put the plotter pen into down position.

Author => Matthew Howard (mah60).
Version =>   0.1 - 18/04/2018 - created the basic Version of the code. This
                        moves the pen to the given location. Then moves it
                        down then up. This will create a dotted print out.
             0.1.1 - 18/04/2018 -  created the plot_neighbour method this will
                        move the pen to the next location. If the current
                        coordinate has a neighbour coordinate.

                        As well, using RR 40 40; command to create squares and
                        given locations instead of dots.
             0.1.2 - 18/04/2018 - removed RR 40 40; as results were
                        unsatisfactory. Sticking with dotting coordinates.
"""
from __future__ import division
from xy_coordinate import XYCoordinate
from serial_control import SerialControl as serial
from plotter_controller import PlotterController
import time
import threading


class DitheringPlotter(PlotterController):
    """
    Summary => will plot the coordinates for the dithering alogorithm.

    Description => will plot the coordinates for the dithering alogorithm style.
                This will be done by sending commands to the plotter. This
                includes the command for HPGL such as;

                PA x y; - this will move the pen to that coordinate
                PU; - put the plotter pen into up position.
                PD; - put the plotter pen into down position.

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
        super(DitheringPlotter, self).__init__(coordinates, scale)

    def run(self):
        """
        Summary => will run the plotter method.

        Description => will run through the coordinates given to the object in
                initialization and plot them in the dithering technique.


        args => None
        return => None
        """
        # get start time of the plot
        self.time_start()
        # select pen 1
        self.ser.write('SP 1;')
        # go through every coordinate in given coordinates
        for point in self.coordinates:
            # check if the coordinate has been plotter. May have
            # already through the plot neighbour method.
            if not point.is_plotted():
                # place pen at this points location
                # need to change coordinates to plotter values.
                # as every 1 coordinate is 40 plotter value.
                x = self.coordinate_to_plotter(point.get_x())
                y = self.coordinate_to_plotter(point.get_y())
                # intergrate values into the correct string format
                str_command = "PA {} {};".format(x, y)
                # send command
                self.ser.write(str_command)
                # put pen down
                self.ser.write('PD;')
                # check if current coordinate has a neighbour.
                self.plot_neighbour(point)
                # put pen up.
                self.ser.write('PU;')
                # mark current coordinate as plotted.
                point.plotted()
        # select pen 0 - so the pen is put that to respected location on the
        # plotter.
        self.ser.write('SP 0;')
        # stop the timer and print out resulting timer.
        self.time_stop()

    def plot_neighbour(self, point):
        """
        Summary => will check if current coordinate has a neighbour.

        Description => will check if the current coordinate has a neighbour.
                as neighbour is if the coordinate is within 1 value to the
                right. Which on the img layout is y value plus one.

                This method includes a recursive loop that will call it
                self if a neighbour is found and plotted to. Then it will
                call itself again to go to the next value.
        args => point - XYCoordinate - the coordinate for the currrent
                        point being looked at.
        return => None
        """
        for move_to in self.coordinates:
            # check if it is the same location as current point
            if point != move_to:
                # check if move_to has already been drawn
                if not move_to.is_plotted():
                    # check move_to coordinate is a neighbour to the point.
                    if (move_to.get_y() == (point.get_y() + 1)) and (
                            move_to.get_x() == point.get_x()):
                        # convert coordinates to plotter values
                        x = self.coordinate_to_plotter(move_to.get_x())
                        y = self.coordinate_to_plotter(move_to.get_y())
                        # create command
                        str_command = "PA {} {};".format(x, y)
                        # send the command through serial.
                        self.ser.write(str_command)
                        # mark the move_to point as plotted. So that point
                        # is not plotted again.
                        move_to.plotted()
                        # create a recursive loop in the method.
                        # to check if the move_to point has a neighbour.
                        self.plot_neighbour(move_to)
