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

    def __init__(self, nbStreets: int, path: list):
        self._path = self.parsePath(path)
        self._position = path[0] if len(path) > 0 else 0
        self._nbStreets = nbStreets

    def parsePath(self, path: list) -> list:

        """Parse the car journey into a list of street.

        Args:
            path (list): list of street's name in which the car has to pass.

        Returns:
            list: The parsed path.
        """

        return [[street, False] for street in path]
