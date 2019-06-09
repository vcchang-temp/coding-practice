# Symmetric tree

# Input: Node root

# Recursive approach
# Time: O(n)  -> must visit every node in each tree
# Space: O(n) -> cal stack memory consumed due to recursion
#                grows to be max n-1 frames (max depth of
#                tree in worst case, aka. straight-line tree) 

from node import Node

def isSymmetric(root: Node):
    return areReflections(root, root)

def areReflections(root1: Node, root2: Node):
    if root1 == None and root2 == None:
        return True
    if root1 == None and root2 != None:
        return False
    if root1 != None and root2 == None:
        return False
    return root1.val == root2.val \
        and areReflections(root1.left, root2.right) \
        and areReflections(root1.right, root2.left)

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