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
from image_proccesor import ImageProccesor
import cv2


class Dithering(ImageProccesor):
    """
    Summary => his class is going to control the proccessing of images.

    Description => This class is going to control the proccessing of images,
                within the program. It will take a the 'takenPicture.jpg'
                from the Image folder and then stlye it. The output
                will be a list of x and y coordinates on the pltter.

    args => None

    None => None
    """

    def __init__(self, ui, ps):
        """
        Summary => will initialize the image proccesor.

        Description => will initialize the images proccesor, to be used later
                    on.

        args => ui -> this is the qt window. The Gui_view

        None => None
        """
        super(Dithering, self).__init__(ui)

        self.ui = ui

        # set the platte_size
        self.platte_size = ps

    def run(self):
        """
        Summary => will find the boarders in the image taken.

        Description =>

        args => None

        None => None
        """
        # get the image to be processed
        img = cv2.imread('Images/takenPicture.jpg', 0)

        img = self.compress_image(img)
        print(img.shape)
        # create a blank img to draw on
        # https://stackoverflow.com/questions/12881926/
        # create-a-new-rgb-opencv-image-using-python
        # blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        # make the image white
        # blank_image[:] = (255, 255, 255)

        img = self.apply_dithering(img)

        self.coordinates = self.calculate_coordinates(img)
        # change the colour pallate, depending on int given
        # img_palatte = self.colour_palatte(self.platte_size, img)

        # create sets to divide divering into
        # dithering_sets = self.dithering_sets(self.platte_size, img)

        cv2.imwrite('Images/proccessedImage.jpg', img)

    def apply_dithering(self, img):

        split = 255/2
        # go through every pixel and apply matrix
        for x in range(0, img.shape[0]):
            for y in range(0, img.shape[1]):
                #print(str(img.item(x, y)) + "--------")
                # change to black
                if img.item(x, y) < split:
                    self.error_defusion(img, x, y, img.item(x, y))
                    img.itemset((x, y), 0)
                else:  # change white
                    self.error_defusion(img, x, y, (img.item(x, y) - 255))
                    img.itemset((x, y), 255)

        return img

    def error_defusion(self, img, x, y, modifier):

        #print(str(int(round(modifier*matrix[2][0])) + img.item(x, y)))

        if self.check_pixel(img, x, y, 0, 1):
            img.itemset((x, y+1), (img.item(x, y+1) + (
                                modifier*(7/16))))
        if self.check_pixel(img, x, y, 1, (-1)):
            img.itemset((x+1, y-1), (img.item(x+1, y-1) + (
                                modifier*(3/16))))
        if self.check_pixel(img, x, y, 1, 0):
            img.itemset((x+1, y), (img.item(x+1, y) + (
                            modifier*(5/16))))
        if self.check_pixel(img, x, y, 1, 1):
            img.itemset((x+1, y+1), (img.item(x+1, y+1) + (
                                modifier*(1/16))))

#    def add_to_pixel(self, img, x, y, change):
#        if change > 255:
#            print(">")
#            change =  change - 255
#           self.add_to_pixel(img, x, y, change)
#        elif change < 0:
#            print("<")
#            change = change + 255
#            self.add_to_pixel(img, x, y, change)
#        else:
#            #print(change)
#            img.itemset((x, y), change)

    def check_pixel(self, img, x, y, x_mod, y_mod):

        if ((x + x_mod) > 0) and ((x + x_mod) < img.shape[0]) and ((
                y + y_mod) > 0) and ((y + y_mod) < img.shape[1]):
            return True
        else:
            return False


    # def calculate_avr_sep(self, img):
    #    average_low = 0
    #    average_high = 0
    #    high_count = 0
    #    low_count = 0
    #    split = 255/2
    #    for x in range(0, img.shape[0]):
    #        for y in range(0, img.shape[1]):
    #            if img.item(x, y) < split:
    #                low_count = low_count + 1
    #                average_low = average_low + img.item(x, y)
    #            else:
    #                high_count = high_count + 1
    #                average_high = average_high + img.item(x, y)
#
#        average_low = average_low / low_count
#        average_high = average_high / high_count
#
#        average = average_low + (average_high - average_low)
#        print(average)
#        return average

#    def colour_palatte(self, kmean, img):
#        """
#        Summary => will find the boarders in the image taken.
#
#        Description =>
#
#        link for code : last seen : 16/04/2018
#        https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_ml/
#        py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html#kmeans-opencv
#
#        args => None
#
#        None => None
#        """
#        Z = img.reshape((-1, 3))
#
#        # convert to np.float32
#        Z = np.float32(Z)
#
#        # define criteria, number of clusters(K) and apply kmeans()
#        criteria = (cv2.TERM_CRITERIA_EPS +
#                    cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#        K = kmean
#        ret, label, center = cv2.kmeans(Z, K, None, criteria, 10,
#                                        cv2.KMEANS_RANDOM_CENTERS)
#
#        # Now convert back into uint8, and make original image
#        center = np.uint8(center)
#        res = center[label.flatten()]
#        res2 = res.reshape((img.shape))
#
#        return res2
#
#    def dithering_sets(self, ps, img):
#        """
#        Summary => will find the boarders in the image taken.
#
#        Description =>
#
#        args => None
#
#        None => None
#        """
#    # generate list of intensities (calculate percentage)/divide to decimal
#        intensity = (100/ps)/100
#        self.ranges = np.zeros((ps+2, 3), dtype=int)
#        # set 0 and 100
#        self.ranges[0][0] = 0  # black
#        self.ranges[0][1] = 0
#        self.ranges[0][2] = 0
#        self.ranges[ps+1][0] = 255  # white
#        self.ranges[ps+1][1] = 255
#        self.ranges[ps+1][2] = ps + 1
#        # generate ranges
#        for i in range(0, ps):
#            value = int(round(255 * (intensity * (i+1))))
#            if i == 0:   # set first range
#                self.ranges[i+1][0] = 1
#                self.ranges[i+1][1] = value
#                self.ranges[i+1][2] = i + 1
#            elif i == (ps-1):  # set last range
#                self.ranges[i+1][0] = self.ranges[i][1]
#                self.ranges[i+1][1] = 254
#                self.ranges[i+1][2] = i + 1
#            else:  # find inbertween ranges
#                self.ranges[i+1][0] = self.ranges[i][1]
#                self.ranges[i+1][1] = value
#                self.ranges[i+1][2] = i + 1

#        print(self.ranges)
#        used_pixels = np.zeros(img.size, dtype=XYCoordinate)
