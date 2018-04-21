"""

Summary => test ImageProccesor.

Description => will test the different methods in ImageProccesor and
            make sure that they are performing the correct functions.

            Will only test the methods needed.

Author => Matthew Howard (mah60).
Version => 0.1 - 21/04/2018 - create the basic set up for testing the
                            ImageProccesor.
           0.2 - 21/04/2018 - removed ui as a args for the proccessors
                        as it is not used.
"""
import unittest
import cv2
import numpy as np

from xy_coordinate import XYCoordinate
from image_proccesor import ImageProccesor


class TestImageProccesor(unittest.TestCase):
    """
    Summary => test PlotterController.

    Description => will test the different methods in plotter controller and
                make sure that they are performing the correct functions.

                Will only test the methods needed

    args => None

    return => None
    """

    @classmethod
    def setUpClass(cls):
        """
        Summary => sets up test resources.

        Description => will set up test resources, this includes a
                proccesor and a blank image. To read and assign values
                to.

        args => None

        return => None
        """
        # create blank opencv image
        cls.blank_image = cv2.imread("Images/blank_image.jpg", 0)
        # create blank image_proccesor
        cls.proccesor = ImageProccesor()
        # add locations to the image
        cls.blank_image.itemset((15, 15), 0)
        cls.blank_image.itemset((18, 15), 0)
        cls.blank_image.itemset((10, 1), 0)
        cls.blank_image.itemset((1, 5), 0)

    def test_calculate_cooridnates(self):
        """
        Summary => test coordinate calculator.

        Description => will test calculate_cooridnates method. By
                creating a blank image and dotting it.

                Then after image is put through the method, check if the
                set coordinates match.

        args => None

        return => None
        """
        # call calculate coordinate method
        self.coords = self.proccesor.calculate_coordinates(self.blank_image)
        # create blank array to match and check values are correct
        blank_array = np.zeros((self.blank_image.size), dtype=XYCoordinate)
        blank_array[0] = XYCoordinate(1, 5)
        blank_array[1] = XYCoordinate(10, 1)
        blank_array[2] = XYCoordinate(15, 15)
        blank_array[3] = XYCoordinate(18, 15)
        # match the two arrays
        for i, coord in enumerate(self.coords):
            # check for zeros
            if not coord == 0:
                self.assertEqual(coord.get_x(), blank_array[i].get_x())
                self.assertEqual(coord.get_y(), blank_array[i].get_y())
            else:
                self.assertEqual(coord, blank_array[i])

    def test_compress_coordinates(self):
        """
        Summary => test commpress_coordinates().

        Description => will test compress_coordinates() method.
                This will be done by calling method on the coordinates
                that were calculated in the previous method. Then
                working out if the size of final array is correct to
                input values.

        args => None

        return => None
        """
        # call calculate coordinate method
        self.coords = self.proccesor.calculate_coordinates(self.blank_image)
        # compress coordinates to remove zero values
        # call get_coordinates as it calls compress_coordinates
        coords = self.proccesor.get_coordinates()
        # count coords
        x = 0
        for i in coords:
            x = x + 1
        # check if the size of the array is equal to 4
        self.assertEqual(x, 4)

    def test_compress_image(self):
        """
        Summary => test compress_image.

        Description => will test compress_image.
                This will be done on the 100x100 image,
                it will be test by seeing the final output of the method
                and seeing if they match up with the correct values.

        args => None

        return => None
        """
        # call compress images on blank image. The final result will be
        # 33 x 33 image when rounded. As it will be compressed by 1/3.
        # blank_image is a 100x100 image.
        img = self.proccesor.compress_image(self.blank_image, 3)
        self.assertEqual(img.shape[0], 33)
        self.assertEqual(img.shape[1], 33)
        # check scaling works by changing method to two making result 50x50
        img = self.proccesor.compress_image(self.blank_image, 2)
        self.assertEqual(img.shape[0], 50)
        self.assertEqual(img.shape[1], 50)

    def test_check_pixel(self):
        """
        Summary => test check_pixel.

        Description => will check_pixel.
                This will check if it is returning the correct values in
                corrispondance of the blank image. This test will give values
                that are outside and within the boundries and see if the true
                or false is correct or not.

        args => None

        return => None
        """
        # check if pixel modifier is within boundries
        self.assertTrue(self.proccesor.check_pixel(
                        self.blank_image, 50, 50, 1, 0))
        # check pixel that are outside boundries
        self.assertFalse(self.proccesor.check_pixel(
                        self.blank_image, 99, 99, 1, 0))


if __name__ == '__main__':
    unittest.main()
