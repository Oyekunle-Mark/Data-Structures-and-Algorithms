from stack import Stack
from queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if self.left is not None:
                return self.left.contains(target)
        else:
            if self.right is not None:
                return self.right.contains(target)

        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            cb(self.left.for_each(cb))
        if self.right:
            cb(self.right.for_each(cb))

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return

        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.len():
            current_node = queue.dequeue()
            print(current_node.value)

            if current_node.left is not None:
                queue.enqueue(current_node.left)

            if current_node.right is not None:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.len():
            current_node = stack.pop()
            print(current_node.value)

            if current_node.left is not None:
                stack.push(current_node.left)

            if current_node.right is not None:
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        stack = Stack()
        stack.push(node)

        while stack.len():
            current_node = stack.pop()
            print(current_node.value)

            if current_node.left is not None:
                stack.push(current_node.left)

            if current_node.right is not None:
                stack.push(current_node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
