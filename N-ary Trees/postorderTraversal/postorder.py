# N-ary postorder traversal
# (Postorder: left, right, root)

# Input: Node root

# Time: O(n)  -> visit every node of arr of len n
# Space: O(n) -> in worst case, tree is linear,
#                ie: root is of n-1 height

from node import Node

def traversePostorder(root: Node):
    if not root:
        return []
    vals = []
    for child in root.children:
        vals.extend(traversePostorder(child))
    vals.append(root.val)
    return vals

if __name__ == "__main__":
    treeNone = None
    expectedNone = []
    actualNone = traversePostorder(treeNone)
    assert actualNone == expectedNone
    print(f"Postorder traversal of tree None: {actualNone}")

    treeOne = Node(1, [])
    expectedOne = [1]
    actualOne = traversePostorder(treeOne)
    assert actualOne == expectedOne
    print(f"Postorder traversal of tree [1]: {actualOne}")

    tree = Node(1, [Node(2, [Node(5, []), Node(6, [])]), Node(3, []), Node(4, [])])
    expected = [5, 6, 2, 3, 4, 1]
    actual = traversePostorder(tree)
    assert actual == expected
    print(f"Postorder traversal of tree [1, 2, 3, 4, 5, 6]: {actual}")