# Max depth of binary tree
# (Note: null root has depth -1; single-noded root
# has depth 0 -> depth = n-1, n = number of nodes)

# Input: Node root

# Iterative approach (level-order traversal)
# Time: O(n)  -> must add every node to deque to find
#                max depth
# Space: O(n) -> create new deque of len n

from node import Node
from collections import deque

def findMaxDepth(root: Node):
    depth = -1
    if not root:
        return depth
    queue = deque([root])
    while queue:
        size = len(queue)
        while size > 0:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            size -= 1
        depth += 1
    else:
        return depth

if __name__ == "__main__":
    rootNone = None
    expectedNone = -1
    actualNone = findMaxDepth(rootNone)
    assert actualNone == expectedNone
    print("Tree of None has no depth.")

    rootOne = Node(1)
    expectedOne = 0
    actualOne = findMaxDepth(rootOne)
    assert actualOne == expectedOne
    print(f"Tree of [1] has depth {actualOne}")

    rootSimple = Node(1)
    rootSimple.left = Node(1)
    rootSimple.right = Node(1)
    expectedSimple = 1
    actualSimple = findMaxDepth(rootSimple)
    assert actualSimple == expectedSimple
    print(f"Tree of [1, 1, 1] has depth {actualSimple}")

    rootComplex = Node(1)
    rootComplex.left = Node(1)
    rootComplex.right = Node(1)
    rootComplex.left.right = Node(1)
    rootComplex.right.left = Node(1)
    rootComplex.right.right = Node(1)
    rootComplex.left.right.left = Node(1)
    rootComplex.left.right.left.left = Node(2)
    expectedComplex = 4
    actualComplex = findMaxDepth(rootComplex)
    assert actualComplex == expectedComplex
    print(f"Tree of [1, 1, 1, None, 1, 1, 1, None, None, 1, None, None, None, None, None, None, None, 2] has depth {actualComplex}")