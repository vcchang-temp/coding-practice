# Binary search (recursive)

# Input: sorted int array arr; int target;
#        int beg; int end

# Time: O(logn)  -> in worst case, arr must be cut into
#                   half until there's only one element
#                   remaining; eg: arr of len 8 will in
#                   worst case be cut into two sets of
#                   4, 2, 1 = 3 times -> same as log2(8)
#                   = 3
# Space: O(logn) -> recursive algorithms require storage
#                   for tasks within tasks within tasks,
#                   and so on, so the space required equals
#                   the depth of the recursion. In binary
#                   search, we make at most logn calls, so
#                   space complexity is the same as the time
#                   complexity in this case = 
#                   O(depth of recursion)

from typing import List
import math

def search(arr: List[int], target: int, beg: int, end: int):
    if beg > end:
        return -1
    mid = math.floor((beg + end) / 2)
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return search(arr, target, mid+1, end)
    else:
        return search(arr, target, beg, mid-1)

if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    target = 2
    actualTwo = search(arr, target, 0, len(arr)-1)
    assert actualTwo == target
    print(f"Hello, is {target} you're looking for? I can see it in your {arr}, using the power of binary search")

    target = 5
    actualMiddle = search(arr, target, 0, len(arr)-1)
    assert actualMiddle == target
    print(f"Hello, is {target} you're looking for? I can see it in your {arr}, using the power of binary search")
    
    target = 0
    actualBeg = search(arr, target, 0, len(arr)-1)
    assert actualBeg == target
    print(f"Hello, is {target} you're looking for? I can see it in your {arr}, using the power of binary search")

    target = 9
    actualEnd = search(arr, target, 0, len(arr)-1)
    assert actualEnd == target
    print(f"Hello, is {target} you're looking for? I can see it in your {arr}, using the power of binary search")

    target = 10
    actualNoTarget = search(arr, target, 0, len(arr)-1)
    assert actualNoTarget == -1
    print(f"Hello, is {target} you're looking for? I can't see it in your {arr}... sorry!")