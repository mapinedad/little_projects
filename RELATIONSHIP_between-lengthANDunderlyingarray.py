import sys


def getsize_underlying_array(n: int):

    data = []
    for k in range(n):
        a = len(data)   # number of elements
        b = sys.getsizeof(data)  # actual size in bytes
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
        data.append(None)


getsize_underlying_array(41)
