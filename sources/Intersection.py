###########################################
#                 HASH CODE               #
###########################################
#                                         #
# Corentin COUTRET-ROZET and Hugo LACHKAR #
#                                         #
###########################################

INCOME = 0
OUTCOME = 1

class Intersection():

    """
    TraficLight class that allows computation and output printing.
    """

    def __init__(self, id: int):
        self._id = id
        self._streets = []
