# Binary search (iterative)

# Input: int array arr, int target

# Time: O(logn) -> in worst case, will have to cut arr
#                  into half until only one element 
#                  remains; can cut arr of len n into 
#                  half max log2(n) times -> O(logn)
# Space: O(1)   -> no extra space needed

from typing import List
import math

def search(arr: List[int], target: int):
    beg = 0
    end = len(arr)-1

    while beg <= end:
        mid = math.floor((beg + end) / 2)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            beg = mid + 1
        else:
            end = mid - 1
    else:
        return -1

if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    target = 2
    actualTwo = search(arr, target)
    assert actualTwo == target
    print(f"Hello, is {target} you're looking for? I can see it in your {arr}, using the power of binary search")

    target = 5
    actualMiddle = search(arr, target)
    assert actualMiddle == target
    print(f"Hello, is {target} you're looking for? I can see it in your {arr}, using the power of binary search")
    
    target = 0
    actualBeg = search(arr, target)
    assert actualBeg == target
    print(f"Hello, is {target} you're looking for? I can see it in your {arr}, using the power of binary search")

    target = 9
    actualEnd = search(arr, target)
    assert actualEnd == target
    print(f"Hello, is {target} you're looking for? I can see it in your {arr}, using the power of binary search")

    target = 10
    actualNoTarget = search(arr, target)
    assert actualNoTarget == -1
    print(f"Hello, is {target} you're looking for? I can't see it in your {arr}... sorry!")