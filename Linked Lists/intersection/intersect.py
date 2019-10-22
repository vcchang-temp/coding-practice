# Intersection of Linked Lists
# Return first intersecting node
# Assume guaranteed that an intersection exists

# Time: O(m + n) -> m = len of list a, n = len of list b
#                   in worst case, ptr belonging to shorter list
#                   travels to end of shorter and longer lists
#                   when no intersection
# Space: O(1)    -> space needed doesn't scale with given inputs
# Explanation -> imagine if the two ptrs had started at the same distance 
#                from the intersection, they would reach the intersection 
#                at the same time, and that's what we want to achieve here
#                with two ptrs. When switching to the longer list, the
#                shorter-list ptr has to travel the difference in length 
#                between the two lists while "waiting" for the longer-list
#                ptr to reach the end of its list; when the longer-list ptr 
#                switches to the shorter list, the two ptrs will be at equal 
#                distances away from the intersection

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def intersect(headA: Node, headB: Node):
    if not headA or not headB:
        return None

    ptrA, ptrB = headA, headB
    while ptrA != ptrB: # exit loop when ptrA, ptrB are None
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA
    return ptrA

if __name__ == "__main__": # TODO Fix examples (alg is right)
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head2 = Node(5)
    head2.next = Node(3)
    head2.next.next = Node(4)
    expected = 3
    actual = intersect(head, head2)
    assert actual.val == expected
    print(f"Yay, found the intersecting node: {actual.val}")

    head = Node(2)
    head2 = Node(5)
    head2.next = Node(2)
    head2.next.next = Node(2)
    expected = 2
    actual = intersect(head, head2)
    assert actual.val == expected
    print(f"Yay, found the intersecting node: {actual.val}")

    head = Node(4)
    head.next = Node(2)
    head.next.next = Node(1)
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