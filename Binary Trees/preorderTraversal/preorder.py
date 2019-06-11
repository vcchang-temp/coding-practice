# Preorder binary tree traversal

# Input: Node root

# Time: O(n)  -> must visit every node
# Space: O(n) -> call stack will have at most n-1 frames
#                (height/max depth of tree)

from node import Node

def traversePreorder(root: Node):
    if not root:
        return []
    vals = []
    vals.append(root.val)
    vals.extend(traversePreorder(root.left))
    vals.extend(traversePreorder(root.right))
    return vals

if __name__ == "__main__":
    treeNone = None
    expectedNone = []
    actualNone = traversePreorder(treeNone)
    assert actualNone == expectedNone
    print(f"Preorder traversal of tree None: {actualNone}")

    treeOne = Node(1)
    expectedOne = [1]
    actualOne = traversePreorder(treeOne)
    assert actualOne == expectedOne
    print(f"Preorder traversal of tree [1]: {actualOne}")

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    expected = [1, 2, 4, 5, 3, 6]
    actual = traversePreorder(tree)
    assert actual == expected
    print(f"Preorder traversal of tree [1, 2, 3, 4, 5, 6]: {actual}")