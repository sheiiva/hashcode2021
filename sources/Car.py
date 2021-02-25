###########################################
#                 HASH CODE               #
###########################################
#                                         #
# Corentin COUTRET-ROZET and Hugo LACHKAR #
#                                         #
###########################################


class Car():

    """
    Car class that allows car informations.
    """

    def __init__(self, path: list, init: int):
        self._path = self.parsePath(path)
        self._position = init

    def parsePath(self, path: list) -> list:

        """Parse the car journey into a list of street.

        Args:
            path (list): list of street's name in which the car has to pass.

        Returns:
            list: The parsed path.
        """

        return [[street, False] for street in path]
