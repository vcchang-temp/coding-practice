# Range sum BST
# Given the root node of a binary search tree, 
# return the sum of values of all nodes with 
# value between L and R (inclusive).

# Assumption: bst is guaranteed to have unique values

# Input: Node bst, int left, int right

# Time: 
# Space: 

from node import Node

def sum(bst: Node, left: int, right: int):

if __name__ == "__main__":
    bstNone = None
    leftNone = 1
    rightNone = 17
    expectedNone = 0
    actualNone = find(bstNone, leftNone, rightNone)
    assert actualNone == expectedNone
    print(f"Range of sum in bst None = {actualNone}")

    bstOne = Node(1)
    leftOne = -1
    rightOne = 2
    expectedOne = 1
    actualOne = find(bstOne, leftOne, rightOne)
    assert actualOne == expectedOne
    print(f"Range of sum in bst [1] = {actualOne}")

    bstComplex = Node(10)
    bstComplex.left = Node(4)
    bstComplex.right = Node(17)
    bstComplex.left.left = Node(2)
    bstComplex.left.right = Node(6)
    bstComplex.right.left = Node(13)
    bstComplex.right.right = Node(21)
    bstComplex.right.right.left = Node(19)
    leftComplex = 6
    rightComplex = 19
    expectedComplex = 6 + 10 + 13 + 17 + 19
    actualComplex = find(bstComplex, leftComplex, rightComplex)
    assert actualComplex == expectedComplex
    print(f"Range of sum in bst [10, 4, 17, 2, 6, 13, 21, None, None, None, None, None, None, 19, None] = {actualComplex}")