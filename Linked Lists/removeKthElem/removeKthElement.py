# Remove k-th Last Element From Linked List

# Time: O(n)  -> traverse at most n elements of list of len n
# Space: O(1) -> storage does not scale with increased input 

# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeKthElement(head: Node, k: int):
    if not head:
        return head
    
    curr = head
    # k = 1, remove head of single-elem list
    if k == 1 and not head.next:
        return None

    while curr and k > 2: # want to stop at node before the one to be removed
        curr = curr.next
        k -= 1

    if not curr or not curr.next: # even if want to remove last elem, would have stopped before curr.next = None
        return head

    toRemove = curr.next
    curr.next = toRemove.next
    toRemove.next = None
    
    return head

def getVals(head: Node):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals

if __name__ == "__main__":
    head = None
    k = 1
    expected = None
    actual = removeKthElement(head, k)
    assert actual == expected
    print(f"Removed {k}st/rd/th element from list!")

    head = Node(1)
    k = 1
    expected = None
    actual = removeKthElement(head, k)
    assert actual == expected
    print(f"Removed {k}st/rd/th element from list!")

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    k = 3
    expectedVals = [1, 2, 4]
    actual = removeKthElement(head, k)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Removed {k}st/rd/th element from list!")

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    k = 4
    expectedVals = [1, 2, 3]
    actual = removeKthElement(head, k)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Removed {k}st/rd/th element from list!")

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    k = 5
    expectedVals = [1, 2, 3, 4]
    actual = removeKthElement(head, k)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Removed {k}st/rd/th element from list!")