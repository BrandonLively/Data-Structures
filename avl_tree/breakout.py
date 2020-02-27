class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)


def get_middle(head):
    """return middle node"""
    node = head
    node_half = head

    # go through all nodes
    while node.next:
        node = node.next
        if node.next:
            # every 2 nodes, update middle
            node = node.next
            node_half = node_half.next

    return node_half


