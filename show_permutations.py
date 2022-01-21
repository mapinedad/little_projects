"""
    Non-recursive algorithm for enumerate all permutations of the {1, 2, ..., n} numbers,
    using explicit stack like S = [1, 2, 3]; note that three elements within S could be different of 1, 2, 3.

    1.- Be S a non-empty stack with {1, 2, 3} elements (n = 3) and Q an empty list,
        and n!=3!=6 the number of permutations of elements in S.
    2.- For i=0 to 5 do:    // for-loop executed six times according to n!=3!=6
    3.-       Show the Stack with element in current order,
    4.-       if i is odd then:
    5.-            while S have some elements do:
    6.-                eliminate element (the last one) from the S and push it into Q (as the last one),
    7.-            while S have only one element in it do:
    8.-                eliminate the first element in Q and push it into S (as the last one).
    9.-        else i is even then:
    10.-            while S have more than one element do:
    11.-                same thing like line 6,
    12.-            while S have only one element in it do:
    13.-                same thing like line 8.

    The output could be something like this:
        1 -> [1, 2, 3]
        2 -> [1, 3, 2]
        3 -> [2, 3, 1]
        4 -> [2, 1, 3]
        5 -> [3, 1, 2]
        6 -> [3, 2, 1]
"""

from ArrayStack import *    # import the ArrayStack self-made class
from math import factorial as fact  # import factorial function from math module


S = ArrayStack()    # empty stack
Q = []  # empty list

for i in range(1, 4):  # Stack: [1, 2, 3]
    S.push(i)
permutations = fact(len(S))  # 3! = 6
# Here's the magic begin!
for i in range(permutations):   # for loop from 0 to 5
    print(f'{i + 1} -> {S}')    # print the stack with element in correspondent order
    if i % 2 != 0:  # check the condition only for odd values of i
        while not S.is_empty():     # while S have some elements
            S_e = S.pop()       # eliminate and return the las element in S
            Q.append(S_e)       # append the S_e to the final of list Q
        while len(S) < 3:       # while len(S) == 1 (that's the meaning)
            Q_e = Q.pop(0)      # eliminate and return the first element on the list Q
            S.push(Q_e)         # push Q_e element into stack S
    else:       # even values of i
        while len(S) > 1:       # while S have more than one element (same operations like lines 44 and 45)
            S_e = S.pop()       
            Q.append(S_e)
        while len(S) < 3:       # same like 46, include the operations
            Q_e = Q.pop(0)
            S.push(Q_e)
