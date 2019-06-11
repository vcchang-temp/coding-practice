# Inorder binary tree traversal

# Input: Node root

# Time: O(n)  -> must visit every node
# Space: O(n) -> call stack will have at most n-1 frames
#                (height/max depth of tree)

from node import Node

def traverseInorder(root: Node):
    if not root:
        return []
    vals = []
    if not root.left and not root.right:
        vals.append(root.val)
    else:
        vals.extend(traverseInorder(root.left))
        if root.val not in vals:
            vals.append(root.val)
        vals.extend(traverseInorder(root.right))
    return vals

if __name__ == "__main__":
    treeNone = None
    expectedNone = []
    actualNone = traverseInorder(treeNone)
    assert actualNone == expectedNone
    print(f"Inorder traversal of tree None: {actualNone}")

    treeOne = Node(1)
    expectedOne = [1]
    actualOne = traverseInorder(treeOne)
    assert actualOne == expectedOne
    print(f"Inorder traversal of tree [1]: {actualOne}")

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    expected = [4, 2, 5, 1, 6, 3]
    actual = traverseInorder(tree)
    assert actual == expected
    print(f"Inorder traversal of tree [1, 2, 3, 4, 5, 6]: {actual}")