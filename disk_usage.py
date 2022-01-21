"""
    A recursive function for reporting disk usage of a file system.
"""

import os


def disk_usage(path):
    """
    Return the number of bytes used by a file/folder and any descendant's.
    """
    total = os.path.getsize(path)  # account for direct usage
    if os.path.isdir(path):  # if this is a directory
        for filename in os.listdir(path):  # then for each child
            child_path = os.path.join(path, filename)  # compose full path to child
            # print(child_path)
            total += disk_usage(child_path)  # add child's usage to total

    print("{0:< 7}".format(total), path)
    return total

if __name__ == '__main__':
    path_ = "/Users/Marcos_Pineda/Documents/SQL Server Management Studio"
    disk_usage(path_)
