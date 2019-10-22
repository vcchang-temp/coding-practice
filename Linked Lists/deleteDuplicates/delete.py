# Delete duplicates

# Time: O(n)  -> move through every node in list of len n
# Space: O(1) -> space needed stays same as inputs grow larger

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head: Node):
    if not head or not head.next:
        return head
        
    a = head
    b = a.next
    
    while b:
        while a.val == b.val:
            if b.next:
                if b.next.val != a.val:
                    a.next = b.next
                    b.next = None
                    b = a.next
                    break
                else:
                    b = b.next
            else:
                a.next = None
                return head
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
    expectedVals = [1, 2]
    actual = deleteDuplicates(head)
    actualVals = getVals(head)
    assert actualVals == expectedVals
    print(f"Removed duplicates from linked list to produce list with unique numbers: {actualVals}")

    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(4)
    expectedVals = [1, 2, 3, 4]
    actual = deleteDuplicates(head)
    actualVals = getVals(head)
    assert actualVals == expectedVals
    print(f"Removed duplicates from linked list to produce list with unique numbers: {actualVals}")