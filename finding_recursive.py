"""
    Recursive program's python for finding the maximum element in a sequence, S, of n elements.
"""


def find_max(sequence, n):
    seq_length = n
    current_max, index = 0, 0

    while index < seq_length:

        if sequence[index] > current_max:

            current_max = sequence[index]

        else:

            find_max(sequence, seq_length - 1)
            index += 1

    return current_max


seq_test = [1, 25000, 3, 4, 5, 450, 2340, 897, 9854, 76545]

print(find_max(sorted(seq_test), len(seq_test)))
