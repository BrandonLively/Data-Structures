from doubly_linked_list.doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.list = DoublyLinkedList()
        self.list_map = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        try:
            result = self.list_map[key].value[1]
            self.list.move_to_front(self.list_map[key])
        except:
            return None
        return result

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        #Modified the add_to_head method to return the head node
        if self.list.length >= self.limit and key not in self.list_map:
            self.list_map.pop(self.list.remove_from_tail()[0], None)
        elif key in self.list_map:
            self.list.delete(self.list_map[key])
        self.list_map[key] = self.list.add_to_head((key, value))
