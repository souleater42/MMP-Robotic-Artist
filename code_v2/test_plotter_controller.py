"""

Summary => test PlotterController.

Description => will test the different methods in plotter controller and
            make sure that they are performing the correct functions.

            Will only test the methods needed.

Author => Matthew Howard (mah60).
Version => 0.1 - 18/03/2018 - create the basic set up for testing the
                            plotter controller.
"""
import unittest

from plotter_controller import PlotterController


class TestPlotterController(unittest.TestCase):
    """
    Summary => test PlotterController.

    Description => will test the different methods in plotter controller and
                make sure that they are performing the correct functions.

                Will only test the methods needed

    Args => None

    Return => None
    """

    # @unittest.skipUnless()
    def test_coordinate_to_plotter(self):
        """
        Summary => test coordinate to plotter.

        Description => will test if the value returned from the
                    coordinate to plotter method is correct.

        Args => None

        Return => None
        """
        # creating the plotter controller, with no coordinates and a scale
        # of 1
        plotter = PlotterController(None, 1)
        # test the coordinate_to_plotter method with the value to. Result
        # should equal 80. As each point on the plotter is 40 and the scale
        # is set to 1.
        result = plotter.coordinate_to_plotter(2)
        self.assertEqual(result, 80)
        # test what the value would be if the scale of the plotter controller,
        # was set to 2. Meaning the value should be devided by 2
        # recreated object
        plotter = PlotterController(None, 2)
        # call command, result should be 40 as the scale devides the final
        # result.
        result = plotter.coordinate_to_plotter(2)
        self.assertEqual(result, 40)


if __name__ == '__main__':
    unittest.main()
