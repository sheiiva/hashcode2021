###########################################
#                 HASH CODE               #
###########################################
#                                         #
# Corentin COUTRET-ROZET and Hugo LACHKAR #
#                                         #
###########################################

from sources.Car import Car
from sources.Street import Street
from sources.Intersection import Intersection, INCOME, OUTCOME


class Trafic():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._info = {}
        self._car = []
        self._intersection = []
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

        def parseStreetInfo(nbStreets: int, infos: list) -> None:

            for i in range(1, nbStreets+1):
                streetInfos = [elem for elem in infos[i].split()]
                self._street.append(Street(int(streetInfos[0]), int(streetInfos[1]),  streetInfos[2], int(streetInfos[3])))

        def parseCarInfo(nbStreets: int, nbCars: int, infos: list) -> None:

            j = 0
            for i in range(-nbCars, 0):
                carInfos = [elem for elem in infos[i].split()]
                self._car.append(Car(int(carInfos[0]), carInfos[1:], j))
                j += 1

        def parseIntersectionInfo(nbIntersection: int, streets: list) -> None:

            for i in range(nbIntersection):
                self._intersection.append(Intersection(i))

            for street in streets:
                for i in range(nbIntersection):
                    if street._end == self._intersection[i]._id:
                        self._intersection[i]._streets.append([street._name, INCOME])
                    elif street._begin == self._intersection[i]._id:
                        self._intersection[i]._streets.append([street._name, OUTCOME])                        

        fileContent = getContent(filename)
        # Parse general informations
        self._info = parseGlobalInfo(fileContent[0])
        # Parse streets informations
        parseStreetInfo(self._info["s"], fileContent)
        # Parse cars informations
        parseCarInfo(self._info["s"], self._info["v"], fileContent)
        # Init trafic lights
        parseIntersectionInfo(self._info["i"], self._street)

    def compute(self):

        def countIncomingStreet(streets):

            counter = 0
            for street in streets:
                if street[1] == INCOME:
                    counter += 1
            return counter

        res = []

        res.append(self._info["i"])
        for intersection in self._intersection:
            res.append(intersection._id)
            res.append(countIncomingStreet(intersection._streets))
            for street in intersection._streets:
                if street[1] == INCOME:
                    res.append(f"{street[0]} 2")

        return res

    def printFile(self, filename: str, output: str) -> None:

        with open(filename, 'w') as f:
            for line in output:
                f.write(f"{str(line)}\n")

    def run(self, args: list) -> None:

        """
        Run computations and process output printing.
        """

        # Parse input arguments
        self.parse(args[1])
        # Compute
        output = self.compute()
        # Print
        self.printFile(f"{args[1][:-4]}_result.txt", output)
