# Same tree
# (tree considered same if structurally the same and
# nodes share same value)

# Input: Node root1, Node root2

# Recursive approach (DFS)
# Time: O(n)  -> must visit and compare every node in each tree
# Space: O(n) -> memory consumed is proportional to height of 
#                tallest tree (n-1 = height of completely skewed 
#                tree; log2(n) = height of full tree)

from node import Node

def isSameTree(p: Node, q: Node):
    if not p and not q:
        return True
    if (not p and q) or (p and not q):
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

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