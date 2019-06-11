# Postorder binary tree traversal

# Input: Node root

# Time: O(n)  -> must visit every node
# Space: O(n) -> call stack will have at most n-1 frames
#                (height/max depth of tree)

from node import Node

def traversePostorder(root: Node):
    if not root:
        return []
    vals = []
    vals.extend(traversePostorder(root.left))
    vals.extend(traversePostorder(root.right))
    vals.append(root.val)
    return vals

if __name__ == "__main__":
    treeNone = None
    expectedNone = []
    actualNone = traversePostorder(treeNone)
    assert actualNone == expectedNone
    print(f"Postorder traversal of tree None: {actualNone}")

    treeOne = Node(1)
    expectedOne = [1]
    actualOne = traversePostorder(treeOne)
    assert actualOne == expectedOne
    print(f"Postorder traversal of tree [1]: {actualOne}")

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    expected = [4, 5, 2, 6, 3, 1]
    actual = traversePostorder(tree)
    assert actual == expected
    print(f"Postorder traversal of tree [1, 2, 3, 4, 5, 6]: {actual}")