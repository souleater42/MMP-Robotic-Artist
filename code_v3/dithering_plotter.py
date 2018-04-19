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
            # place pen at this points location
            x = self.coordinate_to_plotter(point.get_x())
            y = self.coordinate_to_plotter(point.get_y())
            str_command = "PA {} {};".format(x, y)
            self.ser.write(str_command)
            # put pen down
            self.ser.write('PD;')
            self.ser.write('PU;')
        # select pen 0 - so no pen
        self.ser.write('SP 1;')
