"""
    Efficient recursive function for solving the element uniqueness problem, 
    which runs in time that is at most O(n2) in the worst case without using sorting.
"""


def unique(sequence: list) -> bool:
    """Return True if there are no duplicate elements in slice S[start:stop]."""
    for element in sequence:
        n = 0
        if element != sequence[len(sequence) - 1] or len(sequence) == 1:
            print("IF STATEMENT!", element, sequence[len(sequence) - 1])
            return unique(sequence[:n-1])
        else:
            print("ELSE STATEMENT!")
            return False
    return True


def unique2(sequence: list) -> bool:
    pass


seq = [4, -5, 3, -10, 8, 0, 2]
print(unique(seq))