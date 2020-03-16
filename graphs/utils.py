from typing import TypeVar, Generic, Union

T = TypeVar('T')
ReturnedType = Union[T, None]


class Stack(Generic[T]):
    def __init__(self):
        self.stack = []

    def push(self, value: T):
        self.stack.append(value)

    def pop(self) -> ReturnedType:
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self) -> int:
        return len(self.stack)


# A sub-optimal Queue class implementation.
# the class uses a list for storage and pops from the front of the list
# this happens in constant time
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)
