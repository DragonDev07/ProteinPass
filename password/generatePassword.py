import random

def add_symbols(sequence):
	# Change the first 15 C's in the sequence to be an @
	sequence = sequence.replace('C', '@', 15)
	# Change the next 15 C's to be a ^
	sequence = sequence.replace('C', '^', 15)
	# Change the next 15 C's to be a &
	sequence = sequence.replace('C', '&', 15)

	# Return the new sequence with symbols
	return sequence

def add_numbers(sequence):
	# Change the first 5 T's to be a 7
	sequence = sequence.replace('T', '7', 5)
	# Change the next 10 T's to be a random int
	sequence = sequence.replace('T', '69', 10)

	# Return the new sequence with numbers
	return sequence

def add_lowercase(sequence):
	# Change all A's to be a lowercase ('a')
	sequence = sequence.replace('A', 'a')

	# Return the new sequence with lowercase a's
	return sequence