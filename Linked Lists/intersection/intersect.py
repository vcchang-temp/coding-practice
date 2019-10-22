# Intersection of Linked Lists
# Return first intersecting node
# Assume guaranteed that an intersection exists

# Time: O(max(m, n)) -> m = len of a, n = len of b
# Space: O(1)        -> space needed doesn't scale with given inputs

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def intersect(a: Node, b: Node):
    if not a or not b:
        return None

    slow = a
    fast = b
    while slow.val != fast.val:
        fast = fast.next
        if not fast:
            fast = b
        elif fast.val == slow.val:
            return slow
        slow = slow.next
        if not slow:
            slow = a
    return slow

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head2 = Node(5)
    head2.next = Node(4)
    head2.next.next = Node(1)
    expected = 4
    actual = intersect(head, head2)
    assert actual.val == expected
    print(f"Yay, found the intersecting node: {actual.val}")

    head = Node(2)
    head2 = Node(5)
    head2.next = Node(2)
    head2.next.next = Node(1)
    expected = 2
    actual = intersect(head, head2)
    assert actual.val == expected
    print(f"Yay, found the intersecting node: {actual.val}")

    head = Node(4)
    head.next = Node(2)
    head.next.next = Node(3)
    head2 = Node(5)
    head2.next = Node(7)
    head2.next.next = Node(4)
    head2.next.next.next = Node(2)
    head2.next.next.next.next = Node(1)
    expected = 4
    actual = intersect(head, head2)
    assert actual.val == expected
    print(f"Yay, found the intersecting node: {actual.val}")

    head = None
    head2 = Node(5)
    expected = None
    actual = intersect(head, head2)
    assert actual == expected
    print(f"Yay, found the intersecting node: {actual}")