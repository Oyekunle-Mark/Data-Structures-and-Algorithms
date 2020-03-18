from util import Queue

# would hold the words
word_set = set()
# global variable to add words from file to
words = []

# open and file
with open('words.txt', 'r') as f:
    # read all the words, splitting on new lines
    words = f.read().split('\n')

# for every word words
for word in words:
    # add to word_set
    word_set.add(word)

# letters in the English alphabet
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def find_neighbors(word):
    pass

def word_ladder(beginWord, endWord):
    pass
