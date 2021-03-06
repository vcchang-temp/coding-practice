# Max depth of binary tree
# (Note: null root has depth -1; single-noded root
# has depth 0 -> depth = n-1, n = number of nodes)

# Input: Node root

# Recursive approach
# Time: O(n)  -> must visit every node to find max
#                depth
# Space: O(n) -> in worst case, tree is linear and
#                memory consumed on call stack is
#                n-1 frames (again, n-1 = max depth
#                of a linear tree). Best case depth
#                = depth of a full tree = log2(n)

from node import Node

def findMaxDepth(root: Node):
    if not root:
        return -1
    if not root.left and not root.right:
        return 0
    return max(1 + findMaxDepth(root.left), 1 + findMaxDepth(root.right))

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