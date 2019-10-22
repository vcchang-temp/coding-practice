# Remove linked list elements

# Time: O(n)  -> need to traverse entire list of len n
# Space: O(1) -> space needed does not scale with inputs

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElements(head: Node, val: int):
    if not head:
        return head

    a = head
    # special case of head.val == val
    while a.val == val:
        head = a.next
        a.next = None
        a = head
        if not a:
            return head
        
    b = head.next
    # when head.val != val
    while b:
        if b.val == val:
            a.next = b.next
            b.next = None
            b = a.next
            continue
        else:
            a = a.next
            b = b.next
    return head

def getVals(head: Node):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    val = 1
    expectedVals = [2]
    actual = removeElements(head, val)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Removed {val} from linked list to produce: {actualVals}")

    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    val = 2
    expectedVals = [1, 1, 3, 4]
    actual = removeElements(head, val)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Removed {val} from linked list to produce: {actualVals}")

    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    val = 4
    expectedVals = [1, 1, 2, 3]
    actual = removeElements(head, val)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Removed {val} from linked list to produce: {actualVals}")