# Mirror binary tree

# Input: Node root

# Recursive approach
# Time: O(n)  -> must visit every node of tree with n nodes
# Space: O(n) -> memory consumed is at most the depth of the
#                tree -> depth of tree == height of tree ==
#                n-1 nodes -> O(n-1) ~= O(n) space

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def mirror(root: Node):
    if root == None:
        return
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    mirror(root)
    assert root.val == 1
    assert root.left.val == 3
    assert root.right.val == 2
    assert root.left.left.val == 7
    assert root.left.right.val == 6
    assert root.right.left.val == 5
    assert root.right.right.val == 4
    print(f"Tada, the tree with root {root.val} has been inverted!")

    rootNone = None
    mirror(rootNone)
    assert rootNone == None
    print(f"Tada, the tree with root None has been inverted!")

    rootOnlyOne = Node(1)
    mirror(rootOnlyOne)
    assert rootOnlyOne.val == 1
    print(f"Tada, the tree with root {rootOnlyOne.val} has been inverted!")