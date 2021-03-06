# DFS (depth-first search)
# Good for traversing nodes in trees and graphs only once

# Recursive approach
# Time: O(n)  -> visit each node in tree w/ n nodes once
# Space: O(n) -> path list takes up n space.
#                Call stack formed in recursion can take up 
#                - in worst case - n space (tree that's a 
#                straight line), but will in best case take 
#                up logn space for a tree that's completely 
#                filled (ie: last level is completely full). 
#                Otherwise stack also takes up ~O(n) space

from typing import List

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def dfs(root: Node):
    path = []  # could just be a one-liner:
    dfsHelper(root, path) # return dfsHelper(root, [], [])
    return path

def dfsHelper(curr: Node, path: List):
    if not curr:
        return path
    path.append(curr.val)
    if curr.left:
        dfsHelper(curr.left, path)
    if curr.right:
        dfsHelper(curr.right, path)
    return path

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.right = Node(7)
#                1
#              /   \
#            2       3
#          /   \      \
#         4     5      6
#          \
#           7
    expected = [1, 2, 4, 7, 5, 3, 6]
    actual = dfs(root)
    assert actual == expected
    print(f"Awesome, DFS on given binary tree gave: {actual}")

    root = None
    expected = []
    actual = dfs(root)
    assert actual == expected
    print(f"Awesome, DFS on given binary tree gave: {actual}")

    root = Node(17)
    expected = [17]
    actual = dfs(root)
    assert actual == expected
    print(f"Awesome, DFS on given binary tree gave: {actual}")