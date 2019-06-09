# Symmetric tree

# Input: Node root

# Iterative approach
# Time: O(n)  -> must visit every node in each tree
# Space: O(n) -> create new deque of len n (n =
#                number of nodes)

from node import Node
from collections import deque

def isSymmetric(root: Node):
    return areReflections(root, root)

def areReflections(root1: Node, root2: Node):
    queue = deque([(root1, root2)])
    while queue:
        curr1, curr2 = queue.popleft()
        if not curr1 and not curr2:
            continue
        if not curr1 or not curr2:
            return False
        if curr1.val != curr2.val:
            return False
        queue.append((curr1.left, curr2.right))
        queue.append((curr1.right, curr2.left))
    else:
        return True

if __name__ == "__main__":
    rootNone = None
    expectedNone = True
    actualNone = isSymmetric(rootNone)
    assert actualNone == expectedNone
    print("Tree None is symme-tree-c!")

    rootOne = Node(1)
    expectedOne = True
    actualOne = isSymmetric(rootOne)
    assert actualOne == expectedOne
    print("Tree [1] is symme-tree-c!")

    rootSimpleNotSymm = Node(1)
    rootSimpleNotSymm.left = Node(1)
    expectedSimpleNotSymm = False
    actualSimpleNotSymm = isSymmetric(rootSimpleNotSymm)
    assert actualSimpleNotSymm == expectedSimpleNotSymm
    print("Tree [1, 1] is not symme-tree-c!")

    rootComplexNotSymm = Node(1)
    rootComplexNotSymm.left = Node(1)
    rootComplexNotSymm.right = Node(1)
    rootComplexNotSymm.left.right = Node(2)
    rootComplexNotSymm.right.right = Node(2)
    expectedComplexNotSymm = False
    actualComplexNotSymm = isSymmetric(rootComplexNotSymm)
    assert actualComplexNotSymm == expectedComplexNotSymm
    print("Tree [1, 1, 1, None, 2, None, 2] is not symme-tree-c!")

    rootComplexSymm = Node(1)
    rootComplexSymm.left = Node(1)
    rootComplexSymm.right = Node(1)
    rootComplexSymm.left.left = Node(2)
    rootComplexSymm.right.right = Node(2)
    expectedComplexSymm = True
    actualComplexSymm = isSymmetric(rootComplexSymm)
    assert actualComplexSymm == expectedComplexSymm
    print("Tree [1, 1, 1, 2, None, None, 2] is symme-tree-c!")