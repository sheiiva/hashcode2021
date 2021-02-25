###########################################
#                 HASH CODE               #
###########################################
#                                         #
# Corentin COUTRET-ROZET and Hugo LACHKAR #
#                                         #
###########################################

from sources.Car import Car


class Trafic():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._info = 0
        self._car = None
        self._traficLight = None
        self._street = None

    def parse(self, filename: str) -> None:

        def getContent(filename: str) -> list:
            try:
                with open(filename, 'r') as f:
                    return [elem.replace('\n', '') for elem in f.readlines()]
            except:
                print(f"\"{filename}\" no such file.")
                exit(84)

        def parseGlobalInfo(infos: str) -> dict:
            elems = [elem for elem in infos.split()]
            return {"d": elems[0], "i": elems[1], "s": elems[2], "v": elems[3], "f": elems[4]}

        fileContent = getContent(filename)
        # PARSE BELOW
        self._info = parseGlobalInfo(fileContent[0])


    def run(self, args: list) -> None:

        """
        Run computations and process output printing.
        """

        # Parse input arguments
        self.parse(args[1])
        # Compute
        # Print
