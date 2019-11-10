# Middle of the Linked List

# Time: O(n)  -> takes n/2 time to traverse list of len n nodes
# Space: O(1) -> space used does not grow with input (it's constant)

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def middleNode(head: Node):
    slow = fast = head
        
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

if __name__ == "__main__":
    head = Node(1)
    expected = 1
    actual = middleNode(head)
    assert actual.val == expected
    print(f"Found the middle node: {actual.val}")

    head.next = Node(2)
    expected = 2
    actual = middleNode(head)
    assert actual.val == expected
    print(f"Found the middle node: {actual.val}")

    head.next.next = Node(3)
    head.next.next.next = Node(4)
    expected = 3
    actual = middleNode(head)
    assert actual.val == expected
    print(f"Found the middle node: {actual.val}")

    head.next.next.next.next = Node(5)
    expected = 3
    actual = middleNode(head)
    assert actual.val == expected
    print(f"Found the middle node: {actual.val}")
