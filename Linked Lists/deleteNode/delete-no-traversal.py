# Delete Node in Linked List

# No traversal, clever solution
# Time: O(1)  -> only changing pointers
# Space: O(1) -> space needed does not grow with input

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node: Node):
    node.val = node.next.val
    node.next = node.next.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    node = head
    deleteNode(node)
    curr, i = head, 0
    expectedVals = [2]
    while curr:
        assert curr.val == expectedVals[i]
        curr = curr.next
        i += 1
    print(f"Deleted node 1 from list!")

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    node = head.next
    deleteNode(node)
    curr, i = head, 0
    expectedVals = [1, 3, 4]
    while curr:
        assert curr.val == expectedVals[i]
        curr = curr.next
        i += 1
    print(f"Deleted node 2 from list!")