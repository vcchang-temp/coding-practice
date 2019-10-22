# Remove Consecutive Nodes that Sum to 0

# Time: O(n)  -> traverse list at most twice (list len = n) 
# Space: O(n) -> store at most n+1 sums in set

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove(head: Node):
    if not head or not head.next:
        return head

    # special case of two nodes
    if not head.next.next and head.val + head.next.val == 0:
        return None
    
    curr = head
    runningTotal = 0
    sums = set([runningTotal])
    while curr:
        runningTotal += curr.val
        if runningTotal not in sums:
            sums.add(runningTotal)
        else:
            # remove consecutive nodes
            rCurr = head
            rRunningTotal = 0
            rRunningTotal += rCurr.val
            while rRunningTotal != runningTotal:
                rCurr = rCurr.next
                rRunningTotal += rCurr.val
            # remove consecutive nodes' sum
            rCurr2 = rCurr.next
            rRunningTotal += rCurr2.val
            while rRunningTotal in sums:
                sums.remove(rRunningTotal)
                rRunningTotal += rCurr2.val
                rCurr2 = rCurr2.next
            # remove nodes
            if runningTotal == 0: # special case of needing to remove everything from head to node that summed to 0
                head = curr.next
            else:
                last = curr
                curr = curr.next
                rCurr.next = curr
                last.next = None
                continue
        curr = curr.next
    return head

def getVals(head: Node):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(6)
    head.next.next = Node(-3)
    head.next.next.next = Node(-3)
    head.next.next.next.next = Node(1)
    head.next.next.next.next.next = Node(4)
    expectedVals = [1, 1, 4]
    actual = remove(head)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Wooooo removed consecutive nodes summing to 0 to produce: {actualVals}")

    head = Node(1)
    head.next = Node(-1)
    head.next.next = Node(4)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(-2)
    expectedVals = [4, 6, -2]
    actual = remove(head)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Wooooo removed consecutive nodes summing to 0 to produce: {actualVals}")

    head = Node(1)
    head.next = Node(6)
    head.next.next = Node(4)
    head.next.next.next = Node(-2)
    head.next.next.next.next = Node(-2)
    expectedVals = [1, 6]
    actual = remove(head)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Wooooo removed consecutive nodes summing to 0 to produce: {actualVals}")

    head = Node(0)
    head.next = Node(6)
    head.next.next = Node(4)
    expectedVals = [6, 4]
    actual = remove(head)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Wooooo removed consecutive nodes summing to 0 to produce: {actualVals}")

    head = Node(6)
    head.next = Node(0)
    head.next.next = Node(4)
    expectedVals = [6, 4]
    actual = remove(head)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Wooooo removed consecutive nodes summing to 0 to produce: {actualVals}")

    head = Node(2)
    head.next = Node(-2)
    actual = remove(head)
    assert actual == None
    print(f"Wooooo removed consecutive nodes summing to 0 to produce: {actual}")

    head = Node(2)
    head.next = Node(-4)
    expectedVals = [2, -4]
    actual = remove(head)
    actualVals = getVals(actual)
    assert actualVals == expectedVals
    print(f"Wooooo removed consecutive nodes summing to 0 to produce: {actualVals}")