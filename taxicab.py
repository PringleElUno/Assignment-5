# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 10/29/2024
# Define a class named Taxicab that has three private data members: one holding the x-coordinate, one holding,
# one holding the y coordinate, and one holding the current odometer reading

#Define the class

class Taxicab:
    """
    A class to represent the Taxicab's location and track its distance
    """

    def __init__(self, x, y):
        """
        Initializing the taxicab with x and y coordinates and the odometer starting at zero
        :param x: X-coordinate of the taxicab
        :param y: Y-coordinate of the taxicab
        """
        self._x_coord = x
        self._y_coord = y
        self._odometer = 0

    def get_x_coord(self):
        """
        Returns the x-coordinate of the taxicab
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Returns the y-coordinate of the taxicab
        """
        return self._y_coord

    def get_odometer(self):
        """
        Returns the total distance traveled for the odometer
        """
        return self._odometer

    def move_x(self, distance):
        """
        Moves the taxi cab horizontally (the x-axis) by a given distance and updates the odometer
        :param distance: distance to move through the x-axis
        """
        self._x_coord += distance
        self._odometer += abs(distance)

    def move_y(self, distance):
        """
        Moves the taxi cab vertically (the y-axis) by a given distance and updates the odometer
        :param distance: distance to move through the y-axis
        """
        self._y_coord += distance
        self._odometer += abs(distance)