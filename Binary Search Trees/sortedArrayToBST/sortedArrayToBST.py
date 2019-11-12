# Sorted Array to BST

# Time: O(n)  -> visit each num in list of len n once
# Space: O(n) -> recursion creates call stack that in
#                worst case (tree = straight line) is 
#                n frames high

from typing import List
from collections import deque

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def sortedArrayToBST(nums: List[int]):
    if len(nums) == 0:
        return None
        
    mid = (len(nums))//2
    root = Node(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

def bfs(root: Node):
    q, path = deque([root]), []
    while q:
        curr = q.popleft()
        if curr:
            path.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return path

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    expected = [0,-3,9,-10,5]
    actual = sortedArrayToBST(nums)
    assert bfs(actual) == expected
    print(f"Converted sorted array {nums} to BST: {expected}")

    nums = [1]
    expected = [1]
    actual = sortedArrayToBST(nums)
    assert bfs(actual) == expected
    print(f"Converted sorted array {nums} to BST: {expected}")

    nums = []
    expected = []
    actual = sortedArrayToBST(nums)
    assert bfs(actual) == expected
    print(f"Converted sorted array {nums} to BST: {expected}")