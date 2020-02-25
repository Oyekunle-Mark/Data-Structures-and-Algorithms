from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        pass

    def len(self):
        pass
