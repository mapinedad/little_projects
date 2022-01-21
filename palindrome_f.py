"""
    Short recursive Python function that determines if a string s is a palindrome, 
    that is, it is equal to its reverse. 
    
    For example, 'racecar' and 'gohangasalamiimalasagnahog' are palindromes.
"""


def palindrome(S: list, start: int, stop: int) -> bool:

    """
        Return True if S is a palindrome, otherwise print -> Not palindrome!
    """
    if len(S) == 0:
        pass
    elif start < stop - 1:
        try:
            if S[start] != S[stop]:
                exit('Not palindrome!')
            else:
                palindrome(S, start + 1, stop - 1)
                return True
        except (IOError, EOFError, OSError, WindowsError):
            print("INVALID ENTRY! TRY AGAIN...")

if __name__ == '__main__':
    sequence = 'gohangasalamiimalasagnahog'
    is_palindrome = palindrome(list(sequence), 0, len(sequence) - 1)
    print(is_palindrome)