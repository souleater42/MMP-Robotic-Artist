"""
Summary => will apply the dithering algorithm to the image given.

Description => This class is going to control the processing of images for
            the dithering algorithm. It will take a the 'takenPicture.jpg'
            from the Image folder and then stlye it. The output will
            be a list of x and y coordinates for the plotter to print out
            later on.

Author => Matthew Howard (mah60).
Version =>   0.1 - 17/04/2018 - created the basic set up for the dithering
                    class. This includes code to run the algorithm and apply
                    the kernal to the formula.
             0.2 - 18/04/2018 - errors with the diffusion of the code. Meaning
                    the image is comming out incorrectly.

                    Problem solved on the 19/04/2018. -> Was not applying
                    error to correct pixels

                    Removed add_to_pixels method.
            0.3 - 20/04/2018 - working code. Adding comments to the code.
                    Moved check_pixel method to image_processor as the
                    method can be used over all styles written.

                    Removed un-used code. Look at older versions for
                    this code if reqargsred.
             0.3.1 - 21/04/2018 - removed ui from __init_- method as not
                        used
"""
from __future__ import division
from image_processor import ImageProcessor
import cv2


class Dithering(ImageProcessor):
    """
    Summary => will apply the dithering algorithm to the image given.

    Description => This class is going to control the processing of images for
                the dithering algorithm. It will take a the 'takenPicture.jpg'
                from the Image folder and then stlye it. The output will
                be a list of x and y coordinates for the plotter to print out
                later on.

                This class inherits Imageprocessor and will take on the
                individual classes for it.

    args => None

    return => None
    """

    def __init__(self):
        """
        Summary => will initialize the image processor.

        Description => will initialize the images processor, to be used later
                    on.

        args => None

        return => None
        """
        super(Dithering, self).__init__()

    def run(self):
        """
        Summary => will apply the dithering algorithm to the img saved.

        Description => Will apply the Floyd-Steinberg Dithering algorithm
                to the image that was captured in the video capture section.

        args => None

        return => None
        """
        # get the image to be processed, read in gray
        img = cv2.imread('Images/takenPicture.jpg', 0)
        # reduce the size of the image to fit plotter proportions
        img = self.compress_image(img, 3)
        # apply Floyd-Steinberg dithering algorithm
        img = self.apply_dithering(img)
        # calculate coordinates
        self.coordinates = self.calculate_coordinates(img)
        # save the processed image
        cv2.imwrite('Images/processedImage.jpg', img)
        # cv2.imwrite('Images/dithering_example.jpg', img)

    def apply_dithering(self, img):
        """
        Summary => will apply the dithering algorithm to the img given.

        Description => Will apply the Floyd-Steinberg Dithering algorithm
                to the image that was captured in the video capture section.

        args => img -> 2d numpy array - this image will be processed through
                dithering algorithm.

        return => img -> 2d numpy array - this image will be image after
                it has been processed.
        """
        # find even point to split colour values at.
        split = 255/2
        # go through every pixel and apply matrix
        for x in range(0, img.shape[0]):
            for y in range(0, img.shape[1]):
                # print(str(img.item(x, y)) + "--------")
                # change to black
                if img.item(x, y) < split:  # change black
                    # apply error_defusion to surrounding pixels
                    self.error_defusion(img, x, y, img.item(x, y))
                    # change current pixel colour
                    img.itemset((x, y), 0)
                else:  # change white
                    # apply error_defusion to surrounding pixels
                    self.error_defusion(img, x, y, (img.item(x, y) - 255))
                    # change current pixel colour
                    img.itemset((x, y), 255)
        return img

    def error_defusion(self, img, x, y, modifier):
        """
        Summary => will calculate Floyd-Steinberg error defusion method.

        Description => will calculate Floyd-Steinberg error defusion method
                through the dithering algorithm. The process will be done by
                applying the following kernal to the pixels around it.

                0               Current Pixel   modifier*7/16
                modifier*3/16   modifier*5/16   modifier*1/16

                That kernal will go through top left to right of the image
                and add the values to the pixels around it.

        args => img -> 2d numpy array - this image will be processed through
                    dithering algorithm.
                x -> int - x coordinate of the current pixel being looked at.
                y -> int - y coordinate of the current pixel being looked at.
                modifier -> float - This is the value of the current pixel.
                        That will be diffused to the surrounding pixels.
                        Will be negative if closer to 255 and positive if
                        closer to 0.

        return => None
        """
        # check if pixel to the right of current pixel exists.
        if self.check_pixel(img, x, y, 0, 1):
            # set new value for corrisponding pixel exists
            img.itemset((x, y+1), (img.item(x, y+1) + (
                                modifier*(7/16))))
        # check if pixel to the bottom left of current pixel exists.
        if self.check_pixel(img, x, y, 1, (-1)):
            # set new value for corrisponding pixel exists
            img.itemset((x+1, y-1), (img.item(x+1, y-1) + (
                                modifier*(3/16))))
        # check if pixel below the current pixel exists.
        if self.check_pixel(img, x, y, 1, 0):
            # set new value for corrisponding pixel exists
            img.itemset((x+1, y), (img.item(x+1, y) + (
                            modifier*(5/16))))
        # check if pixel to the bottom right of current pixel exists.
        if self.check_pixel(img, x, y, 1, 1):
            # set new value for corrisponding pixel exists
            img.itemset((x+1, y+1), (img.item(x+1, y+1) + (
                                modifier*(1/16))))
