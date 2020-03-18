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
