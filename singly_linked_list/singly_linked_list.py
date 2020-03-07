from typing import TypeVar, Generic, Optional, Any

T = TypeVar('T')


class ListNode(Generic[T]):
    """A single linked list node
    """

    def __init__(self, value: T, next: Optional[Any] = None) -> None:
        self.value = value
        self.next = next

    def get_value(self) -> T:
        return self.value

    def get_next(self) -> Any:
        return self.next

    def set_next(self, next: Any) -> None:
        self.next = next


class LinkedList(Generic[T]):
    """The linked list class
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value: T) -> None:
        new_node = ListNode(value)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self) -> T:
        if not self.head:
            return

        removed_value = self.head.get_value()

        if not self.head.get_next():
            self.head = self.tail = None
        else:
            self.head = self.head.get_next()

        return removed_value

    def contains(self, value: T) -> bool:
        if not self.head:
            return False

        current_node = self.head

        while current_node:
            if current_node.get_value() == value:
                return True

            current_node = current_node.get_next()

        return False

    def print_nodes(self) -> None:
        if not self.head:
            print("Empty")

        nodes = []

        current_node = self.head

        while current_node:
            nodes.append(str(current_node.get_value()))
            current_node = current_node.get_next()

        print(" -> ".join(nodes))


ll = LinkedList()

ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)
ll.add_to_tail(5)

ll.print_nodes()

ll.remove_head()
ll.remove_head()

print(ll.contains(2))

ll.add_to_tail(12)

ll.print_nodes()
