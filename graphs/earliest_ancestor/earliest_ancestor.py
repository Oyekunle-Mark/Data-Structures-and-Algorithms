def find_ancestor(ancestors, num):
    for parent, child in ancestors:
        if child == num:
            return parent

    return -1

def earliest_ancestor(ancestors, starting_node):
    farthest_ancestor = find_ancestor(ancestors, starting_node)

    while farthest_ancestor:
        farthest_ancestor = find_ancestor(ancestors, farthest_ancestor)

    return farthest_ancestor

if __name__ == '__main__':
    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(earliest_ancestor(ancestors, 1))
    print(earliest_ancestor(ancestors, 2))
    print(earliest_ancestor(ancestors, 3))
    print(earliest_ancestor(ancestors, 4))
    print(earliest_ancestor(ancestors, 5))
    print(earliest_ancestor(ancestors, 6))
    print(earliest_ancestor(ancestors, 7))
    print(earliest_ancestor(ancestors, 8))
    print(earliest_ancestor(ancestors, 9))
    print(earliest_ancestor(ancestors, 10))
    print(earliest_ancestor(ancestors, 11))
