# Merge Two Sorted Lists

# Time: O(min(m, n)) -> traverse all nodes of the shortest list
# Space: O(1)        -> output doesn't grow with input

from typing import List

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def mergeTwoLists(l1: Node, l2: Node) -> Node:
    if not l1:
        return l2
    if not l2:
        return l1
    head = None
    if l1.val <= l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next
    curr = head
        
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if not l1:
        curr.next = l2
    if not l2:
        curr.next = l1
    return head

def getVals(head: Node) -> List[int]:
    curr, res = head, []
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

if __name__ == "__main__":
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(6)
    l2 = Node(1)
    l2.next = Node(3)
    l2.next.next = Node(5)
    expectedVals = [1, 1, 2, 3, 5, 6]
    actual = mergeTwoLists(l1, l2)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Merged two linked lists: {actualVals}")