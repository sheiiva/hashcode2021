###########################################
#                 HASH CODE               #
###########################################
#                                         #
# Corentin COUTRET-ROZET and Hugo LACHKAR #
#                                         #
###########################################


class Trafic():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._n = 0
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

        fileContent = getContent(filename)
        # PARSE BELOW

    def run(self, args: list) -> None:

        """
        Run computations and process output printing.
        """

        # Parse input arguments
        self.parse(args[1])
        # Compute
        # Print
