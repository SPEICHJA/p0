"""Grid-world robot controller.

Describe your approach here.

Author: John Speicher

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
    (Describe any help you got.)
"""
from util import Location, get_neighbor

class Robot:
    """A simple Robot in a 2d grid world.

    Provides a public instance variable named `obstacles` that is a
    set containing the coordinates of all obstacles that have been
    observed.

    """

    def __init__(self):
        # Initialize instance variables here.
        pass

    def step(self, loc: Location) -> int:
        """Evaluate the current location and select the next action.

        Parameters:
            loc: a Location is a two-entry tuple where entry 0
                contains x-coordinate and entry 1 contains the y-coordinate.

        Returns:
             An integer in the range 0-3 indicating which direction the robot
             will move.

        """
        # Your controller code will go here.  You are encouraged to
        # create helper methods if you find them useful.

        return 1;

        pass
