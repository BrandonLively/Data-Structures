import sys

from doubly_linked_list.doubly_linked_list import DoublyLinkedList

sys.path.append('../doubly_linked_list')



class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
