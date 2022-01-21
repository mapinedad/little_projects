"""
    Let B be an array of size n ≥ 6 containing integers from 1 to n−5, inclusive,
    with exactly five repeated. Describe a good algorithm for finding the
    five integers in B that are repeated.
"""


def validate_arrayB(array: list) -> bool:
    return len(array) >= 6


def checking_valuesB(array: list, n=1) -> bool:
    lim_inf, lim_sup = 1, n - 5
    for element in array:
        if not lim_inf <= element <= lim_sup:
            return False
        else:
            continue
    return True


def checking_five_repeated(d: dict) -> bool:
    temp = [key for key in d.keys() if d[key] > 1]
    if len(temp) > 5 or len(temp) < 5:
        return False
    else:
        return True


def mapping_repeated_elements(array: list) -> dict:
    elements_mapped = {x: array.count(x) for x in array}
    return elements_mapped


def showing_repeated_values(d: dict):
    print(f'The five elements repeated are: {[key for key in d.keys() if d[key] > 1]}')


"""for the test
B = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8, 2, 10, 11, 11, 11, 12, 12, 14, 15]

if validate_arrayB(B) and checking_valuesB(B, len(B)):
    D = mapping_repeated_elements(B)
    if checking_five_repeated(D):
        showing_repeated_values(D)
else:
    print(f'The Array {B} have values that not match on interval 1 - {len(B) - 5}'
          f'or the length of {B} are less than six elements.')
"""