###########################################
#                 HASH CODE               #
###########################################
#                                         #
# Corentin COUTRET-ROZET and Hugo LACHKAR #
#                                         #
###########################################


class Street():

    """
    Street class that allows street informations and computation.
    """

    def __init__(self, b: int, e: int, name: str, l: int):
        self._begin = b
        self._end = e
        self._name = name
        self._length = l #length in seconds
