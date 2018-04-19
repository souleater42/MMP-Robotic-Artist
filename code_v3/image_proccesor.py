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

    None => None
    """

    def __init__(self, ui):
        """
        Summary => will initialize the image proccesor.

        Description => will initialize the images proccesor, to be used later
                    on.

        args => ui -> this is the qt window. The Gui_view

        None => None
        """
        self.ui = ui

    def boarders(self):
        """
        Summary => will find the boarders in the image taken.

        Description => will find the boarders in the image take, using
                opencv. The will work by making the image graystyle, then
                using a GaussianBlur to filter the image. Then using sobal
                to calculate where the edges are.

                After this we use a threshold to swap the black and white
                colours around.

        args => None

        None => None
        """
        # get the image to be processed
        img = cv2.imread('Images/takenPicture.jpg', 0)
        # img_edges = cv2.Canny(img, 80, 80)
        # blur the image so we can tell where the key boarders are
        blur = cv2.GaussianBlur(img, (9, 9), 0)
        # create a sobal diratives
        sobal = cv2.Sobel(blur, cv2.CV_64F, 1, 1, ksize=5)
        # convert the sobal diratives to canny_style
        # to view the edges of the image
        # sobalCopy = np.uint8(sobal) #  https://stackoverflow.com/questions
        # /19103933/depth-error-in-2d-image-with-opencv-python
        # canny = cv2.Canny(img, 25, 100, L2gradient=False)
        # save the final output
        # change image type to unit 8
        sobal = np.uint8(sobal)
        # creates a threshold to create a black and white image
        ret, threshold = cv2.threshold(sobal, 25, 255, cv2.THRESH_BINARY_INV)

        cv2.imwrite("Images/proccessedImage.jpg", threshold)

        self.calculate_coordinates(threshold)

    def calculate_coordinates(self, img):
        """
        Summary => calculate where the coordinates are.

        Description => will search through the image given and calculate where,
                the individual coordinates are by looking at the pixels and
                working out where the black pixels are.

        args => img => this is a jpg image and has a dtype8.

        None => None
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

        # print(self.coordinates[i - 1])

    def get_coordinates(self):
        """
        Summary => returns the current set of coordinates.

        Description => will return the current set of coordinates that
                needs to be printed.

        args => None
        None => None
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

        None => None
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
        print(img.shape)
        height = int(round(img.shape[0]/2))
        width = int(round(img.shape[1]/2))
        print(str(height) + "," + str(width))
        resized_image = cv2.resize(img, (width, height))
        return resized_image


#class ColourSets(object):
#        """
#        Summary => his class is going to control the proccessing of images.
#
#        Description =>
#
#        args => None
#
#        None => None
#        """

#        def __init__(self, set):
#            """
#            Summary => will initialize the image proccesor.
#
#            Description => will initialize the images proccesor, to be used later
#                        on.

#            args => None
#
#            None => None
#            """
#            self.set = set

#        def generate_boarder(self):
#            """
#            Summary => will initialize the image proccesor.

#            Description => will initialize the images proccesor, to be used later
#                        on.

#            args => None

#            None => None
#            """
