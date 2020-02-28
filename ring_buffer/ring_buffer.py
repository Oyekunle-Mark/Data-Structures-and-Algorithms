from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the length of the DoublyLinkedList/dll is less than the capacity
            # add the item to the tail
            # set the current to the tail of the dll
        # if the length of the dll is equivalent to the capacity of the buffer
            # if the current node is the tail of the dll
                # set the current to the head of the dll
            # otherwise,
                # set the current to the next node after it

            # set the value of current to the item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
