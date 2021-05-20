# Letter Boxed Solver
Solve the NYTimes Letter Boxed puzzle https://www.nytimes.com/puzzles/letter-boxed

This works for any n-sided puzzle with any number of letters on a side, although the NYTimes puzzles seem to always be 4 sides of 3 letters each.

## Algorithm
1. Filter the dictionary for words that satisfy the specified groups of letters ('sides') and adjacency rules
2. For each of the valid dictionary words, do a depth-first search, recursively adding each possible next word to the sequence
  - Next words must begin with the last letter of the previous word; use a dictionary of `first_letter --> [words]` to make this efficient 
  - Begin with a max depth of 1 (ie single-word solutions to the puzzle), then increase depth until solutions are found. This is effectively a breadth-first search, albeit one that discards work from the previous step; if going deeper than ~3 levels with the standard 4-sides-of-3-letters puzzle, this should be reimplemented as breadth-first search
3. If a valid solution is found, ie a sequence of words that uses all letters in the puzzle, add it to the list
4. Print solutions for that depth and increase the allowed sequence length if none were found

## Setup
Install Python 3.x 

You will also need a dictionary of possible words to search. Larger word lists are more likely to include words considered invalid by NYTimes. 
* 58k word list: http://www.mieliestronk.com/corncob_lowercase.txt
* 480k word list: https://github.com/dwyl/english-words/blob/master/words.txt

## Usage
For a puzzle with sides JNS, AEU, GMW, DTI:
```
python letter-boxed.py -w ~/Downloads/words.txt -s jns aeu gmw dti 
```
Output:
```
sides: ['jns', 'aeu', 'gmw', 'dti']
checking for 1-word solutions
  found 0 solutions
checking for 2-word solutions
  found 15 solutions
    ['adjustment', 'twanging']
    ['adjustment', 'twig']
    ['adjustment', 'twigs']
    ['adjustment', 'twinge']
    ['adjustment', 'twinges']
    ['adjustment', 'twining']
    ['adjustments', 'sawing']
    ['adjustments', 'sewing']
    ['adjustments', 'sewings']
    ['adjustments', 'stewing']
    ['adjustments', 'swing']
    ['adjustments', 'swingeing']
    ['adjustments', 'swinging']
    ['adjustments', 'swings']
    ['judgements', 'sawing']
```
