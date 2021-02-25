###########################################
#                 HASH CODE               #
###########################################
#                                         #
# Corentin COUTRET-ROZET and Hugo LACHKAR #
#                                         #
###########################################


def isInt(item) -> bool:

    """Define if item is an integer or not.

    Args:
        item (?): Variable to check.

    Returns:
        bool: True if item is an integer, False otherwise.
    """

    try:
        int(item)
    except ValueError:
        return False
    else:
        return True


def isFloat(item) -> bool:

    """Define if item is an float or not.

    Args:
        item (?): Variable to check.

    Returns:
        bool: True if item is an float, False otherwise.
    """

    try:
        float(item)
    except ValueError:
        return False
    else:
        return True


def removeDup(myList: list) -> list:

    res = []

    [res.append(x) for x in myList if x not in res]
    return res


def isFile(filename: str) -> bool:

    """Define if a file exists or not.

    Args:
        filename (str): File to check.

    Returns:
        bool: True if filename is a true file, False otherwise.
    """

    try:
        open(filename, "r")
    except FileNotFoundError:
        return False
    else:
        return True
