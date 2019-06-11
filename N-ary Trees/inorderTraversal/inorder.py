# N-ary inorder traversal
# (Inorder: left, root, right)

# Input: Node root

# Time: O(n)  -> visit every node of arr of len n
# Space: O(n) -> in worst case, tree is linear,
#                ie: root is of n-1 height

from node import Node

def traverseInorder(root: Node):
    if not root:
        return []
    vals = []
    if not root.children:
        vals.append(root.val)
    else:
        for child in root.children:
            vals.extend(traverseInorder(child))
            if root.val not in vals:
                vals.append(root.val)
    return vals

if __name__ == "__main__":
    treeNone = None
    expectedNone = []
    actualNone = traverseInorder(treeNone)
    assert actualNone == expectedNone
    print(f"Inorder traversal of tree None: {actualNone}")

    treeOne = Node(1, [])
    expectedOne = [1]
    actualOne = traverseInorder(treeOne)
    assert actualOne == expectedOne
    print(f"Inorder traversal of tree [1]: {actualOne}")

    tree = Node(1, [Node(2, [Node(5, []), Node(6, [])]), Node(3, []), Node(4, [])])
    expected = [5, 2, 6, 1, 3, 4]
    actual = traverseInorder(tree)
    assert actual == expected
    print(f"Inorder traversal of tree [1, 2, 3, 4, 5, 6]: {actual}")