# Same tree
# (tree considered same if structurally the same and
# nodes share same value)

# Input: Node p, Node q

# Iterative approach (DFS)
# Time: O(n)  -> must visit and compare every node in each tree
# Space: O(n) -> create stack with at most n-1 nodes (max depth/
#                height of tree; ie: worst case of straight line)

from node import Node

def isSameTree(p: Node, q: Node):
    stack = [(p, q)]
    while stack:
        n1, n2 = stack.pop()
        if not n1 and not n2:
            continue
        if (n1 and not n2) or (not n1 and n2):
            return False
        if n1.val != n2.val:
            return False
        if n1 and n2:
            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))
    return True

if __name__ == "__main__":
    root1None = None
    root2None = None
    expectedBothNone = True
    actualBothNone = isSameTree(root1None, root2None)
    assert actualBothNone == expectedBothNone
    print(f"The trees None and None are the same!")
    
    root1None = None
    root2 = Node(1)
    expectedOneNone = False
    actualOneNone = isSameTree(root1None, root2)
    assert actualOneNone == expectedOneNone
    print(f"The trees None and [1] are not the same!")

    root1 = Node(1)
    root2None = None
    expectedOneNone = False
    actualOneNone = isSameTree(root1, root2None)
    assert actualOneNone == expectedOneNone
    print(f"The trees [1] and None are not the same!")

    root1Same = Node(1)
    root1Same.left = Node(2)
    root1Same.right = Node(3)
    root1Same.left.left = Node(4)
    root1Same.right.right = Node(5)
    root2Same = Node(1)
    root2Same.left = Node(2)
    root2Same.right = Node(3)
    root2Same.left.left = Node(4)
    root2Same.right.right = Node(5)
    expectedSame = True
    actualSame = isSameTree(root1Same, root2Same)
    assert actualSame == expectedSame
    print(f"The trees [1, 2, 3, 4, None, None, 5] and [1, 2, 3, 4, None, None, 5] are the same!")

    root1NotSame = Node(1)
    root1NotSame.left = Node(2)
    root1NotSame.right = Node(3)
    root1NotSame.left.left = Node(4)
    root2NotSame = Node(1)
    root2NotSame.left = Node(2)
    root2NotSame.right = Node(3)
    expectedNotSame = False
    actualNotSame = isSameTree(root1NotSame, root2NotSame)
    assert actualNotSame == expectedNotSame
    print(f"The trees [1, 2, 3, 4] and [1, 2, 3] are not the same!")