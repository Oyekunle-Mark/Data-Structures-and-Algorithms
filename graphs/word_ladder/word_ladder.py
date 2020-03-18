from util import Queue

word_set = set()
words = []

with open('words.txt', 'r') as f:
    words = f.read().split('\n')

for word in words:
    word_set.add(word)

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def find_neighbors(word):
    pass

def word_ladder(beginWord, endWord):
    pass
