"""
	﻿Short Python function that takes a string s, representing a sentence,
	and returns a copy of the string with all punctuation removed. For example, 
	if given the string "Let's try, Mike.", this function would return "Lets try Mike".
"""


def removed_punctuation(sequence):
    punctuation = dict({ord(a): None for a in ({chr(a) for a in range(33, 48, 1)}
                                               | {chr(a) for a in range(58, 65, 1)}
                                               | {chr(a) for a in range(91, 97, 1)}
                                               | {chr(a) for a in range(123, 127, 1)})})
    return sequence.translate(punctuation)
