"""
    Use recursion to write a Python function for determining if a string S has more vowels than consonants.
"""


def remove_whitespace(string: str) -> str:
    """
        This function replace whitespaces for void string -> ''

        Input: string with (or without) whitespace
        Output: string without whitespace
    """
    try:
        if len(string) == 0 or (len(string) == 1 and string != ' '):
            return string.lower()
        else:
            new_string = string.replace(' ', '').replace('(', '').replace(')', '').replace('.', '').replace(',', '')
            return new_string.lower()
    except TypeError:
        exit('Invalid entry...')


def vowels_consonants(S: list, stop: int, v_dict: dict, c_dict: dict) -> dict:
    """
        This function count the vowels and consonants in the list S (note S is a list of letters in any string given),
        using a dictionary (built-in data structure, -dict-) and later return a tuple with two dictionary's,
        one for vowels and other for consonants.

        Note: this function call itself n-1 times for a list (S) of length n (n-1 = stop).

        Input: list 'S', top of the list 'stop' and two dictionary's one for vowels and other for consonants
        (which are used for counting the number of vowels and consonants on S).
        Output: a tuple of two dictionary's.
    """
    if len(S) == 0:
        return None
    else:
        if S[stop - 1] in v_dict.keys():
            v_dict[S[stop - 1]] += 1
        else:
            c_dict[S[stop - 1]] += 1
        if stop > 0:
            vowels_consonants(S, stop - 1, v_dict, c_dict)
    return v_dict, c_dict


def more_vowel_than_consonants(vowel_dict: dict, consonant_dict: dict) -> bool:
    """
        Function that returns a boolean value, indicating if an string have more vowels than consonants.

        Input: two dictionary's -> vowel_dict, consonant_dict.
        Output: True if number of vowels are greater than number of consonants. Neither return False. (Boolean type).
    """
    more_vowels = sum(vowel_dict.values()) > sum(consonant_dict.values())
    if more_vowels:
        return True
    elif not more_vowels:
        return False


if __name__=='__main__':

    vowels = {x: 0 for x in {'a', 'e', 'i', 'o', 'u'}}
    consonants = {x: 0 for x in set(chr(y) for y in range(97, 123, 1)).difference({'a', 'e', 'i', 'o', 'u'})}

    word = sorted(list(remove_whitespace('Each element of the list will result in a bit memory address being stored in the primary array, '
                                         'and an int instance being stored elsewhere in memory. Python allows you to query '
                                         'the actual number of bytes being used for the primary storage of any object. This '
                                         'is done using the get size of function of the sys module. On our system, the size of '
                                         'a typical int object requires  bytes of memory (well beyond the bytes needed '
                                         'for representing the actual bit number). In all, the list will be using bytes per '
                                         'entry, rather than the bytes that a compact list of integers would require.')))
    top_word_list = len(word) - 1
    vowels_consonants_dicts = vowels_consonants(word, top_word_list, vowels, consonants)
    print(more_vowel_than_consonants(vowels_consonants_dicts[0], vowels_consonants_dicts[1]))
