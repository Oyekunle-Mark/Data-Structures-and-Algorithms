# '''
# Linked List hash table key/value pair
# '''
from typing import Any


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key: Any):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key: Any):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # set a variable hash to the prime number
        hash = 5381

        # loop through every character in the string
        for c in key:
            # set hash to the sum of  5 bitwise shift left operation on hash plus hash
            # plus the character code of the present character
            hash = ((hash << 5) + hash) + ord(c)

        # return hash and bitwise and the hexadecimal constant 0xFFFFFFFF
        return hash & 0xFFFFFFFF

    def _hash_mod(self, key: Any) -> int:
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity

    def insert(self, key: Any, value: Any) -> None:
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # get the index
        index = self._hash_mod(key)
        # create the new node
        new_node = LinkedPair(key, value)

        # if there is no item at the index
        if self.storage[index] is None:
            # place the new node
            self.storage[index] = new_node
        # otherwise,
        else:
            # point current to the head
            current = self.storage[index]

            # if the current node's key is equivalent to key
            if current.key == key:
                # update the value with value
                current.value = value
                # return
                return

            # loop while current's next is not None
            while current.next:
                # move current to the next node
                current = current.next

                # if the current node's key is equivalent to key
                if current.key == key:
                    # update the value with value
                    current.value = value
                    # return
                    return

            # point the tail's next to the new node
            current.next = new_node

    def remove(self, key: Any) -> None:
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # get the index
        index = self._hash_mod(key)

        # if there is no item at the index
        if self.storage[index] is None:
            # print a warning
            print("Key does not exist in the Hash Table")
            # return
            return
        # otherwise,
        else:
            # point current to the head
            current = self.storage[index]

            # if head is the one to be removed
            if current.key == key:
                # if head does not have a next node
                if current.next is None:
                    # set the current index of storage to None
                    self.storage[index] = None
                    # return
                    return
                # otherwise,
                else:
                    # point the current index of storage to the next item after the head
                    self.storage[index] = current.next

            # loop while current has a next node
            while current.next:
                # set previous to the current node
                prev = current
                # set next to the next node
                current = current.next

                # if current node's key is equivalent to key
                if current.key == key:
                    # if current key is the tail
                    if current.next is None:
                        # point previous node to None
                        prev.next = None
                    # otherwise,
                    else:
                        # point previous node's next to the current node's next
                        prev.next = current.next

    def retrieve(self, key: Any) -> Any:
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # get the index
        index = self._hash_mod(key)

        # if there is not item at the index
        if self.storage[index] is None:
            # return  None
            return None
        # otherwise,
        else:
            # point current to the head
            current = self.storage[index]

            # while current is not None
            while current:
                # if the current's node key is equivalent to key
                if current.key == key:
                    # return the value
                    return current.value

                # move current to the next node
                current = current.next

            # return None if no key matches key
            return None

    def resize(self) -> None:
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double the capacity
        self.capacity *= 2
        # grab a pointer to the old store
        old_store = self.storage
        # point the storage to a new list of twice the size of the old
        self.storage = [None] * self.capacity

        # loop through every item in old_store
        for item in old_store:
            # of item is not None
            if item is not None:
                # point current to the head
                current = item

                # loop while there is a node
                while current:
                    # insert the current's node key, value pair into the storage
                    self.insert(current.key, current.value)
                    # move current to the next node
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
