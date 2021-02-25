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

    def __init__(self, d: int, b: int, e: int, name: str):
        self._length = d #length in seconds
        self._begin = b
        self._end = e
        self._name = name
