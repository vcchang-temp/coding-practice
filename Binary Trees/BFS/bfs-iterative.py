# BFS (breadth-first search)
# Good for traversing nodes in trees and graphs only once
# Better than DFS for finding shortest path to a node from
# an arbitrary node (b/c you won't be travelling deep into
# one or more paths that may not take you to the node for 
# which you're looking)

# Iterative approach
# Time: O(n)  -> visit each node in tree w/ n nodes once
# Space: O(n) -> path list and queue each take up n space

# Note about recursive approach: since BFS uses a queue to
# determine which node to visit next, it'd be difficult to
# implement BFS recursively without a queue since recursion 
# relies on the stack data structure which operates in an 
# opposite manner to a queue. For example, DFS lends itself 
# naturally to how a stack operates and can therefore rely
# on a running computer program's call stack. (In DFS, we
# visit the last node that we've visited to process and then
# to determine the next node to visit, a "greedy" order which
# takes us deeper and deeper down a tree.)

from typing import List
from collections import deque

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def bfs(root: Node):
    q = deque([root])
    path = []

    while q:
        curr = q.popleft()
        if curr and curr not in path:
            path.append(curr)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    
    return [n.val for n in path]

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
    expected = [1, 2, 3, 4, 5, 6, 7]
    actual = bfs(root)
    assert actual == expected
    print(f"Awesome, BFS on given binary tree gave: {actual}")

    root = None
    expected = []
    actual = bfs(root)
    assert actual == expected
    print(f"Awesome, BFS on given binary tree gave: {actual}")

    root = Node(17)
    expected = [17]
    actual = bfs(root)
    assert actual == expected
    print(f"Awesome, BFS on given binary tree gave: {actual}")