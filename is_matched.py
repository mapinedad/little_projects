"""
    Function for matching delimiters in an arithmetic expression
"""


from ArrayStack import *


def is_matched(expr):
    """
        Return True if all delimiters are properly match; False otherwise
    """
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


es = is_matched('[(5+x)-(y+z)]')
print(es)
