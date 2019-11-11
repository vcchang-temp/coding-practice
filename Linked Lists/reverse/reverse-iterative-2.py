# Reverse a singly linked list

# Input: Node head (could be null or of any length)

# Iterative approach 2
# Time: O(n)    -> traverse list with n nodes once
# Space: O(1)   -> in-place reversal

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head: ListNode):
    if not head or not head.next:
        return head
        
    prev = head
    curr = head.next
    next = head.next.next
        
    prev.next = None
        
    while next:
        curr.next = prev
        prev = curr
        curr = next
        next = curr.next
    else:
        curr.next = prev
        prev = None
        head = None
        
    return curr

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