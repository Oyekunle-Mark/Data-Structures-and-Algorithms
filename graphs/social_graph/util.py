from typing import TypeVar, Generic, Union

T = TypeVar('T')
ReturnedType = Union[T, None]


# A sub-optimal Queue class implementation.
# the class uses a list for storage and pops from the front of the list
# this happens in constant time
class Queue(Generic[T]):
    def __init__(self):
        self.queue = []

    def enqueue(self, value: T) -> None:
        self.queue.append(value)

    def dequeue(self) -> ReturnedType:
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self) -> int:
        return len(self.queue)
