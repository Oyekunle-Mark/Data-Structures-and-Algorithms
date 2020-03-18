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
    # would hold the generated word neighbors
    neighbors = []

    # for each character position in word
    for index in range(len(word)):
        # convert the word to list as a new copy
        word_list = list(word)

        # for every letter in the English alphabet
        for letter in LETTERS:
            # replace the current index with current letter
            word_list[index] = letter
            # join to form a new word
            new_word = ''.join(word_list)

            # if the new word is not the input word and word is in word_set
            if new_word != word and new_word in word_set:
                # add it to neighbors
                neighbors.append(new_word)

    # return neighbors
    return neighbors

def find_word_ladders(beginWord, endWord):
    """
    Uses Breadth-First Search(BFS) to find the transformation sequence of a word
    from beginWord to endWord.
    """
    visited = set()
    queue = Queue()
    queue.enqueue([beginWord])

    while queue.size():
        path = queue.dequeue()
        current_word = path[-1]

        if current_word == endWord:
            return path

        if current_word not in visited:
            visited.add(current_word)

            for word in find_neighbors(current_word):
                new_path = list(path)
                new_path.append(word)
                queue.enqueue(new_path)

    return None


if __name__ == '__main__':
    print(find_word_ladders("hit", "cog"))
    print(find_word_ladders("sail", "boat"))
    print(find_word_ladders("hungry", "happy"))
