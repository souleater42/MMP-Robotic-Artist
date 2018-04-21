"""
Summary => This class will be used to store x and y values.

Description => will store x and y value, in a more suitable format. This
        format will make it easier to store and transfer the x,y coordinate
        for each point more easily. There is a getter and setter for the
        x and y values given. As well, will print out as "x-value,y-value"
        when printed.

Author => Matthew Howard (mah60).
Version => 0.1 - 15/03/2018 - created the basic set up for the xy-coordinate
                class. This include a methods to get and set the x and y
                vaulues in the object. There is as well a methods to print The
                coordinates out.
           0.2 - 18/03/2018 - removed the num_connections, as is not needed.
           0.3 - 19/03/2018 - changed the names of drawn and is_drawn to
           plotter and is_plotter. Otherwise, when drawn() was called.
           It would overight the drawn varible. As they had the same name.

"""


class XYCoordinate(object):
    """
    Summary => This class will be used to store x and y values.

    Description => will store x and y value, in a more suitable format. This
            format will make it easier to store and transfer the x,y coordinate
            for each point more easily. There is a getter and setter for the
            x and y values given. As well, will print out as "x-value,y-value"
            when printed.

    args => x - int - this is the x coordinate
            y - int - this is the y coordinate

    return => None
    """

    def __init__(self, x, y):
        """
        Summary => will create a object with x and y values.

        Description => will create a object with x and y values. The x and y
            values will be the vaulues given in the args above.

            Each coordinate has the num of connections connected to this
            coordinate. Near the grid.

            if connection is 0 -> the point is by it self. Else if
            1 -> there is one line connection.

        args => x - int - value of x-coordinate
                y - int - value of y-coordinate

        return => None
        """
        self.x = x
        self.y = y
        self.drawn = False

    def get_x(self):
        """
        Summary => returns x.

        Description => returns the x coordinate for this object.

        args => None

        return => x - int - this is the x coordinate for this object.
        """
        return self.x

    def get_y(self):
        """
        Summary => returns y.

        Description => returns the y coordinate for this object.

        args => None

        return => y - int - this is the x coordinate for this object.
        """
        return self.y

    def set_x(self, x):
        """
        Summary => will set the x value, for this coordinate.

        Description => will take the x value given and set this objects x
        coordinate for this object to that value.

        args => x - this is what you want to change the x coordinate to for
                this object to.

        return => None
        """
        self.x = x

    def set_y(self, y):
        """
        Summary => will set the y value, for this coordinate.

        Description => will take the y value given and set this objects x
        coordinate for this object to that value.

        args => y - this is what you want to change the y coordinate to for
                this object to.

        return => None
        """
        self.y = y

    def is_plotted(self):
        """
        Summary => checks if this coordinate has been plotted.

        Description => checks if this coordinate has been plotted. Will
                return true, if it has been fully drawn.

        args => None

        return => boolean - true - has been plotted.
                          - false -  has not been plotted yet.
        """
        return self.drawn

    def plotted(self):
        """
        Summary => mark this coordinate as drawn.

        Description => marks this coordinate as drawn, so that this
                coordinate will not be drawn again on the plotting
                device.

        args => None

        return => None
        """
        self.drawn = True

    def __str__(self):
        """
        Summary => will print out the coordinate inside this object.

        Description => will print out the coordinate inside this object
        as the string "x-value,y-value".

        args => None

        return => String - this is a string for the current object.
        """
        return str(self.x) + "," + str(self.y)
