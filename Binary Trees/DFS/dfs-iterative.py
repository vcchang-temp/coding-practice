# DFS (depth-first search)
# Good for traversing nodes in trees and graphs only once

# Iterative approach
# Time: O(n)  -> visit each node in tree w/ n nodes once
# Space: O(n) -> path list takes up n space.
#                Stack can also take up - in worst case -
#                n space (tree that's a straight line),
#                but will in best case take up logn space
#                for a tree that's completely filled (ie:
#                last level is completely full). Otherwise
#                stack also takes up ~O(n) space

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def dfs(root: Node):
    stack = [root]
    path = []
    
    while stack:
        curr = stack.pop()
        if not curr:
            continue
        path.append(curr.val)
        if curr.right: # start w/ right to visit left child first when pop off stack
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)  
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