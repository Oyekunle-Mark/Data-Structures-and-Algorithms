def find_ancestor(ancestors, num):
    for parent, child in ancestors:
        if child == num:
            return parent

    return -1

def earliest_ancestor(ancestors, starting_node):
    pass
