import argparse
from collections import defaultdict
import re

# Ruin the Letter Boxed puzzle https://www.nytimes.com/puzzles/letter-boxed
#
# Usage (requires python 3+):
#
#	python letter-boxed.py -w ~/Downloads/words.txt -s jns aeu gmw dti 
#
# Word lists:
# - 480k word list: https://github.com/dwyl/english-words/blob/master/words.txt
# - 58k word list: http://www.mieliestronk.com/corncob_lowercase.txt
# 

ap = argparse.ArgumentParser()
ap.add_argument('-w', '--word_file', required=True, help='path to word list')
ap.add_argument('-s', '--side', nargs='+', required=True, help='sequence of letters on a side')
args = vars(ap.parse_args())

# For each letter, determine the letters that are allowed to follow it, ie the letters on other sides
def get_complements(sides):
	complements = {}
	for side in sides:
		other_sides = [s for s in sides if s != side]
		other_letters = ''.join(other_sides)
		for char in side:
			complements[char] = other_letters
	return complements

# Filter a list of words to find those that are valid based on the given sides
def find_matching_words(words, sides):
	complements = get_complements(sides)
	matching_words = []
	for w in words:
		word = w.strip().lower()
		next_chars = complements.get(word[0])
		for i in range(1, len(word)):
			if len(word) >= 3 and next_chars and word[i] in next_chars:
				next_chars = complements.get(word[i])
			else:
				break
			if i == len(word) - 1:
				matching_words.append(word)
	return matching_words

# When a word is used, subtract it from the required letters left to be used
def get_remaining_letters(word, letters):
	 return re.sub(r'[%s]'%(word), '', letters)

# Create a dictionary from a character to words starting with that character
def get_words_by_first_char(words):
	d = defaultdict(list)
	for word in words:
		first_char = word[0]
		d[first_char].append(word)
	return d

# Add a word to the current sequence and recurively add words to the sequence until
#	- all required letters have been used by the sequence (indicating a valid solution)
#	- max depth is hit (puzzle can typically be solved in a 2-3 word sequence)
def add_word_to_sequence(word, sequence, all_letters, valid_sequences, max_depth, words_by_first_char):
	if word in sequence:
		return
	remaining_letters = get_remaining_letters(word, all_letters)
	sequence.append(word)
	last_char = word[len(word) - 1]
	if (len(remaining_letters) == 0):
		valid_sequences.append(sequence)
		return 
	elif len(sequence) >= max_depth:
		return
	else:
		next_words = words_by_first_char.get(last_char)
		for next_word in next_words:
			add_word_to_sequence(next_word, sequence.copy(), remaining_letters, valid_sequences, max_depth, words_by_first_char)

def main():
	# Pre-process / build all the helper data structures
	sides = args['side']
	words = open(args['word_file'], 'r').readlines()
	matching_words = find_matching_words(words, sides)
	words_by_first_char = get_words_by_first_char(matching_words)
	complements = get_complements(sides)
	all_letters = ''.join(sides)

	# Find solutions, starting with depth of 1 (single word) and increasing allowed sequence length
	print('sides: %s' % (sides))
	for max_depth in range(1,4):
		print('checking for %i-word solutions' % (max_depth))
		valid_sequences = []
		for word in matching_words:
			add_word_to_sequence(word, [], all_letters, valid_sequences, max_depth, words_by_first_char)
		print('  found %i solutions' % (len(valid_sequences)))
		for sequence in valid_sequences:
			print('    %s' % (sequence))
		if valid_sequences:
			return

if __name__ == "__main__":
    main()




