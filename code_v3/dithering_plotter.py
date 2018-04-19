"""
Summary => his class is going to control the proccessing of images.

Description => This class is going to control the proccessing of images, within
            the program. It will take a the 'takenPicture.jpg' from the Image
            folder and then stlye it. The output will be a list of x and y
            coordinates on the pltter.

Author => Matthew Howard (mah60).
Version =>   0.1 -
"""
from __future__ import division
from xy_coordinate import XYCoordinate
from serial_control import SerialControl as serial
from plotter_controller import PlotterController
from time import sleep


class DitheringPlotter(PlotterController):
    """
    Summary => his class is going to control the proccessing of images.

    Description => This class is going to control the proccessing of images,
                within the program. It will take a the 'takenPicture.jpg'
                from the Image folder and then stlye it. The output
                will be a list of x and y coordinates on the pltter.

    args => None

    None => None
    """

    def __init__(self, coordinates, scale):
        """
        Summary => will initialize the image proccesor.

        Description => will initialize the images proccesor, to be used later
                    on.

        args => ui -> this is the qt window. The Gui_view

        None => None
        """
        super(DitheringPlotter, self).__init__(coordinates, scale)

        self.ser = serial("/dev/ttyUSB0")
        self.coordinates = coordinates
        self.scale = scale

    def run(self):
        # select pen 1
        self.ser.write('SP 1;')
        for point in self.coordinates:
            if not point.is_plotted():
                # place pen at this points location
                x = self.coordinate_to_plotter(point.get_x())
                y = self.coordinate_to_plotter(point.get_y())
                str_command = "PA {} {};".format(x, y)
                self.ser.write(str_command)
                # put pen down
                self.ser.write('PD;')
                pix_size = int(round(40/self.scale))
                #sleep(1)
                #str_command = "RR {} {}".format(pix_size, pix_size)
                #self.ser.write(str_command)
                self.plot_neighbour(point)
                self.ser.write('PU;')
                point.plotted()
        # select pen 0 - so no pen
        self.ser.write('SP 1;')

    def plot_neighbour(self, point):
        for move_to in self.coordinates:
            # check if it is the same location as current point
            if point != move_to:
                # check if move_to has already been drawn
                if not move_to.is_plotted():
                    if (move_to.get_y() == (point.get_y() + 1)) and (
                            move_to.get_x() == point.get_x()):
                        x = self.coordinate_to_plotter(move_to.get_x())
                        y = self.coordinate_to_plotter(move_to.get_y())
                        str_command = "PA {} {};".format(x, y)
                        self.ser.write(str_command)
                        #pix_size = int(round(40/self.scale))
                        #str_command = "RR {} {}".format(pix_size, pix_size)
                        #self.ser.write(str_command)
                        move_to.plotted()
                        self.plot_neighbour(move_to)
