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
    """
    Find all the possible neighbors of a word by replacing each letters 
    in the word with every letter in the English alphabet and confirming if
    the generated word can be found in word_set. It returns all the possible neighbors
    as a list of strings
    """
    pass

def word_ladder(beginWord, endWord):
    """
    Uses Breadth-First Search(BFS) to find the transformation sequence of a word
    from beginWord to endWord.
    """
    pass
