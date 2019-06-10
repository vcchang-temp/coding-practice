# N-ary preorder traversal
# (Preorder: root, left, right)

# Input: Node root

# Time: O(n)  -> visit every node of arr of len n
# Space: O(n) -> in worst case, tree is linear,
#                ie: root is of n-1 height

from node import Node

def traversePreorder(root: Node):
    if not root:
        return []
    vals = []
    vals.append(root.val)
    for child in root.children:
        vals.extend(traversePreorder(child))
    return vals

if __name__ == "__main__":
    treeNone = None
    expectedNone = []
    actualNone = traversePreorder(treeNone)
    assert actualNone == expectedNone
    print(f"Preorder traversal of tree None: {actualNone}")

    treeOne = Node(1, [])
    expectedOne = [1]
    actualOne = traversePreorder(treeOne)
    assert actualOne == expectedOne
    print(f"Preorder traversal of tree [1]: {actualOne}")

    tree = Node(1, [Node(2, [Node(5, []), Node(6, [])]), Node(3, []), Node(4, [])])
    expected = [1, 2, 5, 6, 3, 4]
    actual = traversePreorder(tree)
    assert actual == expected
    print(f"Preorder traversal of tree [1, 2, 3, 4, 5, 6]: {actual}")