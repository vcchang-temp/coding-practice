# Reverse a singly linked list

# Input: Node head (could be null or of any length)

# Recursive approach
# Time: O(n)    -> traverse list with n nodes twice
# Space: O(n)   -> 

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head: ListNode):
    if not head or not head.next:
        return head

    # n = points at same node as head when recursive call returns;
    # we'll make n.next.next point back to itself to form a loop
    # then we break the loop by setting n.next = None
    # eg: 1 -> 2, head, n = Node(1)
    #     ------
    #     |    |
    #     v    |
    #     1 -> 2  head.next.next = head
    #     1 <- 2  head.next = None
    n = reverse(head.next)
    head.next.next = head
    head.next = None
    return n

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    head = node1
    actual = reverse(head)

    node1Rev = ListNode(1)
    node2Rev = ListNode(2)
    node3Rev = ListNode(3)
    node4Rev = ListNode(4)
    node4Rev.next = node3Rev
    node3Rev.next = node2Rev
    node2Rev.next = node1Rev
    expected = node4Rev

    testActual = actual
    testExpected = expected
    while testActual is not None:
        assert testActual.val == testExpected.val
        testActual = testActual.next
        testExpected = testExpected.next
    
    print("Yayy, reversed a linked list!")