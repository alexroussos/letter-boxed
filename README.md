# spelling-bee
Solve the NYTimes Letter Boxed puzzle https://www.nytimes.com/puzzles/letter-boxed

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
