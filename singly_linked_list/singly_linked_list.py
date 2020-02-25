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
        new_node = ListNode(value)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return

        removed_value = self.head.get_value()

        if not self.head.next():
            self.head = self.tail = None
        else:
            self.head = self.head.next

        return removed_value

    def contains(self, value):
        pass
