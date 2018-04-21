"""
Summary => his class is going to control the proccessing of images.

Description => This class is going to control the proccessing of images, within
            the program. It will take a the 'takenPicture.jpg' from the Image
            folder and then stlye it. The output will be a list of x and y
            coordinates on the pltter.

Author => Matthew Howard (mah60).
Version =>   0.1 - 12/03/2018 - set up basic set up for the class
             0.1.1  - 01/04/2018 - moved image loader to styling methods. This
                        is because it caused error in loading wrong image, when
                        doing it in the initialization stage.
             0.2 - 11/04/2018 - created a method that will find the boarders
                        in the image taken. Then we can calculate where the
                        coordinates are by looking at the individual pixels.
             0.3 - 15/04/2018 - changed code to support python2 instead of
                        python3. No changes needed.
             0.3.1 - 15/04/2018 - created a method to compress the
                        self.coordinates array. To remove any unwanted values.
             0.3.2 - 16/04/2018 - created a ColourSets class to control to
                        create areas where the pixels in that area had the
                        same colour. Going to use for dithering.
             0.4 - 17/04/2018 - created the methods compress_image to reduce
                        the size of images handed to it. As well, made
                        this class a parent class. In which stlye proccessing
                        will be inheriting this class.

                        commented out colour sets class as the class is not
                        required for the dithering algorithm.
             0.4.1 - 20/04/2018 - moved the check_pixel method to
                        ImageProccesor class as it will be used generically
                        throughout other classes as well.

                        created run() method that will tell the user that
                        the proccessor is incorrect.
"""
from xy_coordinate import XYCoordinate
import numpy as np
import cv2


class ImageProccesor(object):
    """
    Summary => his class is going to control the proccessing of images.

    Description => This class is going to control the proccessing of images,
                within the program. It will take a the 'takenPicture.jpg'
                from the Image folder and then stlye it. The output
                will be a list of x and y coordinates on the pltter.

    args => None

    return => None
    """

    def __init__(self, ui):
        """
        Summary => will initialize the image proccesor.

        Description => will initialize the images proccesor, to be used later
                    on.

        args => ui -> this is the qt window. The Gui_view

        return => None
        """
        self.ui = ui

    def run(self):
        """
        Summary => running a blank proccesor.

        Description => will print error message. As they are running a black
                proccesor.

        args => None

        return => None
        """
        print("-------------------------------------------------------")
        print("error: procccessor is empty.")
        print("       Advice:")
        print("              procccessor is wrong type.")
        print("-------------------------------------------------------")

    def calculate_coordinates(self, img):
        """
        Summary => calculate where the coordinates are.

        Description => will search through the image given and calculate where,
                the individual coordinates are by looking at the pixels and
                working out where the black pixels are.

        args => img => this is a jpg image and has a dtype8.

        return => None
        """
        # generate x and y coordinates
        self.coordinates = np.zeros(img.size, dtype=XYCoordinate)
        i = 0
        # loop through x values
        for x in range(0, img.shape[0]):
            # loop through y values
            for y in range(0, img.shape[1]):
                # if the pixel is coloured black, create a new coord to
                # add to the numpy array.
                if img.item(x, y) == 0:
                    self.coordinates[i] = XYCoordinate(x, y)
                    i = i + 1
        return self.coordinates
        # print(self.coordinates[i - 1])

    def get_coordinates(self):
        """
        Summary => returns the current set of coordinates.

        Description => will return the current set of coordinates that
                needs to be printed.

        args => None
        return => None
        """
        self.compress_coordinates()

        return self.coordinates

    def compress_coordinates(self):
        """
        Summary => compress the array of coordinates.

        Description => will compress the numpy array of coordinates, to
                    remove all zeros.

                    Zeros are the slots that are not being used in the
                    array.

        args => None

        return => None
        """
        # count all the values that are not zero
        i = 0
        for coord in self.coordinates:
            if coord != 0:
                i = i + 1
        # create new numpy array to replace self.coordinates
        new_coord = np.zeros(i, dtype=XYCoordinate)
        # fill the new array of coordinates.
        for x in range(0, i):
            new_coord[x] = self.coordinates[x]
        # replace old coordinates array with new one without empty slots
        self.coordinates = new_coord

    def compress_image(self, img):
        """
        Summary => compress the size of the image given.

        Description => will change the size of the image by 1/3 of its
                original size. This is done using opencv.

                The scale was determined by the resolution of the camera
                it was taken in and then reduced down to fit onto the plotters
                scale.

        args => img -> opencv image. This will be a numpy array format.

        return => resized_image -> image when it has been resized
        """
        # print(img.shape)
        # calculate the height and width of new compress_image
        # the size will be 1/3 of its original size.
        height = int(round(img.shape[0]/3))
        width = int(round(img.shape[1]/3))
        # print(str(height) + "," + str(width))
        # use opencv to resize the image given.
        resized_image = cv2.resize(img, (width, height))
        return resized_image

    def check_pixel(self, img, x, y, x_mod, y_mod):
        """
        Summary => checks if the given pixel exists.

        Description => checks if the given pixels exists and returns True. If
                it does.

        args => img -> 2d numpy array - this image will be processed through
                    dithering algorithm.
                x -> int - x coordinate of the current pixel being looked at.
                y -> int - y coordinate of the current pixel being looked at.
                x_mod -> int - the modifier for the pixel that is wanting to
                    be looked at from the current pixel.
                y_mod -> int - the modifier for the pixel that is wanting to
                    be looked at from the current pixel.

        return => None
        """
        # check if the pixel wanting to be looked at is within the boundries
        # of the image that is given.
        if ((x + x_mod) > 0) and ((x + x_mod) < img.shape[0]) and ((
                y + y_mod) > 0) and ((y + y_mod) < img.shape[1]):
            return True
        else:
            return False
