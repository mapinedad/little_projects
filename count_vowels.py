"""
	﻿Short Python function that counts the number of vowels in a given character string.
"""

def count_vowels(sequence_str: str) -> int:
	letters = list(sequence_str.lower())	# convert string to list in wich all elements are lowercase letter
	vowels = set('aeiou')		# set of vowels to comparate
	count_vowel = set()
	for letter in letters:		# for each letter in letters check if letter is in set vowels
		if letter in vowels:
			count_vowel.add(letter)		# adding letter to the set count_vowel
		else: 
			continue		# otherwise move on to next letter
	return len(list(count_vowel))	# return the total of vowels in sequence_str