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
        return self.coordinates
