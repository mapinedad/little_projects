def reverse(S, start, stop):
    """
        Reverse elements in implicit slice S[start:stop] -- LINEAR RECURSION
    """

    if start < stop - 1:  # if at least 2 elements:
        S[start], S[stop - 1] = S[stop - 1], S[start]  # swap first and last.
        reverse(S, start + 1, stop - 1)
        return S


def binary_sum(S, start, stop):
    """
        Return the sum of the numbers in implicit slice S[start:stop] -- BINARY RECURSION
    """
    if start >= stop:  # zero elements in slice
        return 0
    elif start == stop - 1:  # one element in slice
        return S[start]
    else:  # two or more elements in slice
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


sequence = [x for x in range(1, 10)]

print(reverse(sequence, 0, len(sequence)))

print(binary_sum(sequence, 0, len(sequence)))
