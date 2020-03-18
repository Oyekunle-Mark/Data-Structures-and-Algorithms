def find_ancestor(ancestors, num):
    """
    Takes the ancestors list and a num and returns the first ancestor
    of num from the list of ancestors
    """
    # loop for every parent child
    for parent, child in ancestors:
        # if the child is the same as num
        if child == num:
            # then parent is found, return it
            return parent

    # otherwise, no parent found, return None
    return None

def earliest_ancestor(ancestors, starting_node):
    """
    Finds the earliest ancestor of starting node. Works by performing
    a BFS until the parent has no parent itself. If two parents are both the
    earliest, the first(left most) is chosen because the graph has some form of order.
    """
    farthest_ancestor = find_ancestor(ancestors, starting_node)

    if farthest_ancestor is None:
        return -1

    while True:
        if find_ancestor(ancestors, farthest_ancestor) is None:
            return farthest_ancestor

        farthest_ancestor = find_ancestor(ancestors, farthest_ancestor)



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
