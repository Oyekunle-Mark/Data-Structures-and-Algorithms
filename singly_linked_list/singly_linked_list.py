class ListNode:
    """A single linked list node
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList:
    """The linked list class
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        pass

    def remove_head(self):
        pass

    def contains(self, value):
        pass
