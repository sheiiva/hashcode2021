###########################################
#                 HASH CODE               #
###########################################
#                                         #
# Corentin COUTRET-ROZET and Hugo LACHKAR #
#                                         #
###########################################

from sources.Car import Car
from sources.Street import Street


class Trafic():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._info = 0
        self._car = None
        self._traficLight = None
        self._street = []

    def parse(self, filename: str) -> None:

        def getContent(filename: str) -> list:
            try:
                with open(filename, 'r') as f:
                    return [elem.replace('\n', '') for elem in f.readlines()]
            except:
                print(f"\"{filename}\" no such file.")
                exit(84)

        def parseGlobalInfo(infos: str) -> dict:
            elems = [int(elem) for elem in infos.split()]
            return {"d": elems[0], "i": elems[1], "s": elems[2], "v": elems[3], "f": elems[4]}

        def parseStreetInfo(nbStreets: int, infos: str) -> None:

            for i in range(1, nbStreets+1):
                streetInfos = [elem for elem in infos[i].split()]
                self._street.append(Street(int(streetInfos[0]), int(streetInfos[1]),  streetInfos[2], int(streetInfos[3])))


        fileContent = getContent(filename)
        # Parse general informations
        self._info = parseGlobalInfo(fileContent[0])
        # Parse streets informations
        parseStreetInfo(self._info["s"], fileContent)


    def run(self, args: list) -> None:

        """
        Run computations and process output printing.
        """

        # Parse input arguments
        self.parse(args[1])
        # Compute
        # Print
