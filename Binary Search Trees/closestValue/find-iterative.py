# Closest value in BST
# (BST = tree in which all left children of a node
# are always guaranteed to be less than value stored
# in node and all right children are guaranteed to
# to be equal or greater than value stored in node)

# Input: BST bst

# Assumption: there is guaranteed to be a single, 
#             unique value

# Iterative approach
# Time: O(n)  -> in worst case, tree is linear 
#                (n-1 height)
# Space: O(1) -> space does not grow with input;
#                only need a local variable to 
#                store closest value

from node import Node
import math

def find(bst: Node, target: int):
    closestVal = math.inf
    while bst:
        if abs(target - closestVal) > abs(target - bst.val):
            closestVal = bst.val
        if target > bst.val:
            bst = bst.right
        elif target < bst.val:
            bst = bst.left
        else:
            break
    return closestVal

if __name__ == "__main__":
    bstNone = None
    targetNone = 17
    expectedNone = math.inf
    actualNone = find(bstNone, targetNone)
    assert actualNone == expectedNone
    print(f"Yus, got the closest value in BST: {actualNone}")

    bstOne = Node(1)
    targetOne = 17
    expectedOne = 1
    actualOne = find(bstOne, targetOne)
    assert actualOne == expectedOne
    print(f"Yus, got the closest value in BST: {actualOne}")

    bst = Node(8)
    bst.left = Node(5)
    bst.right = Node(17)
    bst.left.left = Node(4)
    bst.left.right = Node(7)
    bst.right.left = Node(14)
    bst.right.right = Node(21)
    bst.right.right.left = Node(18)
    target = 12
    expected = 14
    actual = find(bst, target)
    assert actual == expected
    print(f"Yus, got the closest value in BST: {actual}")