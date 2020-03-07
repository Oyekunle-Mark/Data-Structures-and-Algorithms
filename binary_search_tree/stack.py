from typing import TypeVar, Generic
from doubly_linked_list import DoublyLinkedList

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value: T) -> None:
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self) -> T:
        if self.size:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self) -> int:
        return self.size
