from typing import TypeVar, Generic, Optional, Any, Union

T = TypeVar('T')


class ListNode(Generic[T]):
    """Each ListNode holds a reference to its previous node
    as well as its next node in the List."""

    def __init__(self, value: T, prev: Optional[Any] = None, next: Optional[Any] = None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value: T) -> None:
        current_next = self.next
        self.next = ListNode(value, self, current_next)

        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value: T) -> None:
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)

        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self) -> None:
        if self.prev:
            self.prev.next = self.next

        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList(Generic[T]):
    def __init__(self, node: Optional[ListNode] = None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self) -> int:
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value: T) -> None:
        new_node = ListNode(value)

        if not self.head and not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self) -> T:
        if not self.head and not self.tail:
            return

        removed_node_value = self.head.value

        if self.head is self.tail:
            self.head = self.tail = None
        else:
            removed_node = self.head
            self.head = self.head.next
            removed_node.delete()

        self.length -= 1
        return removed_node_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value: T) -> None:
        new_node = ListNode(value)

        if not self.head and not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self) -> T:
        if not self.head and not self.tail:
            return

        removed_node_value = self.tail.value

        if self.head is self.tail:
            self.head = self.tail = None
        else:
            removed_node = self.tail
            self.tail = self.tail.prev
            removed_node.delete()

        self.length -= 1
        return removed_node_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node: ListNode) -> None:
        if node == self.head:
            return

        node_value = node.value

        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

        self.add_to_head(node_value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node: ListNode) -> None:
        if node is self.tail:
            return

        node_value = node.value

        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1

        self.add_to_tail(node_value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node: ListNode) -> None:
        if node is self.head:
            self.remove_from_head()
        elif node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self) -> Union[None, T]:
        if not self.head:
            return None

        current_max_value = self.head.value
        current_node = self.head

        while current_node:
            if current_node.value > current_max_value:
                current_max_value = current_node.value

            current_node = current_node.next

        return current_max_value
