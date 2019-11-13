# Binary Tree Level Order Traversal II

# Time: O(n)  -> visit every node in tree with n nodes once
# Space: O(n) -> create dictionary with lists containing total 
#                n nodes

from node import Node
from collections import deque

def levelOrderBottom(root: Node):
    if not root:
        return []
                
    q = deque([(root, 0)])
    d_n = {}
        
    while q:
        n, d = q.popleft()
        if d in d_n:
            temp = d_n[d]
            temp.append(n.val)
            d_n[d] = temp
        else:
            d_n[d] = [n.val]
        if n.left:
            q.append((n.left, d+1))
        if n.right:
            q.append((n.right, d+1))
        
    res = []
    for d in reversed(range(len(d_n))):
        res.append(d_n[d])
        
    return res

if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    expected = [[15,7],[9,20],[3]]
    actual = levelOrderBottom(root)
    assert actual == expected
    print(f"Traversed tree from bottom-up: {actual}")