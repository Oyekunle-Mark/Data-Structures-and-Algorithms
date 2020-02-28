from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the length of the DoublyLinkedList/dll is less than the capacity
        if self.storage.length < self.capacity:
            # add the item to the tail
            self.storage.add_to_tail(item)
            # set the current to the tail of the dll
            self.current = self.storage.tail
        # if the length of the dll is equivalent to the capacity of the buffer
        if self.storage.length == self.current:
           # if the current node is the tail of the dll
            if self.current == self.storage.tail:
                # set the current to the head of the dll
                self.current = self.storage.head
            # otherwise,
            else:
                # set the current to the next node after it
                self.current = self.current.next

            # set the value of current to the item
            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # set the current_node to the head of the dll
        # loop while there is a current_node
            # append the value of the current node to the list
            # set the current node to the next node

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
