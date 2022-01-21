"""
    C-5.25 The syntax data.remove(value) for Python list data removes only the first
    occurrence of element value from the list. Give an implementation of a
    function, with signature remove_all(data, value), that removes all occurrences
    of value from the given list.
"""


from random import shuffle


def remove_all(data: list, value: object):

    try:

        if value not in data:
            print(f'Value {value} not in data list {data}')

        else:

            while value in data:
                data.pop(data.index(value))

        return data

    except (ValueError, IndexError, TypeError, SystemError) as Error:
        print(f"An error was occur...{Error}")


def remove_all_2(data: list, value: object):
    try:

        if value not in data:
            print(f'Value {value} not in data list {data}')

        else:

            while value in data:
                del data[data.index(value)]

        return data

    except (ValueError, IndexError, TypeError, SystemError) as Error:
        print(f"An error was occur...{Error}")