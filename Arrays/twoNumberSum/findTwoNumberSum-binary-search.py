# Two number sum
# (return sorted array of the two ints that make up the 
# target sum if can find target sum; otherwise return 
# empty array)

# Binary search approach
# Input: non-empty array with distinct integers arr,
# integer target sum targetSum

# Assumptions: arr is sorted

# Time: O(logn) -> binary search cuts number of search 
#                  items in half in each iteration; runtime
#                  equals number of times array is divided 
#                  = log2(n)
#                  eg: n = 8 
#                      8 -> 4 -> 2 -> 1
#                      log2(8) = 3
# Space: O(1)   -> results array of len 2

from typing import List
import math

def findTwoNumberSum(arr: List[int], targetSum: int):
    result = []
    for i in range(len(arr)-1):
        diff = targetSum - arr[i]
        idx = binarySearch(arr, diff, i+1, len(arr)-1)
        if idx == -1:
            continue
        else:
            result.append(arr[i])
            result.append(arr[idx])
            break
    return result

def binarySearch(arr: List[int], diff: int, beg: int, end: int):
    mid = math.floor((beg + end) / 2)
    if arr[mid] == diff:
        return mid
    if beg >= end:
        return -1
    if arr[mid] > diff:
        return binarySearch(arr, diff, beg, mid-1)
    else:
        return binarySearch(arr, diff, mid+1, end)

if __name__ == "__main__":
    arr = [-4, -1, 0, 1, 2, 3, 6, 7]
    targetSum1 = -1
    expected = [-4, 3]
    actual = findTwoNumberSum(arr, targetSum1)
    assert actual == expected
    print(f"Found the two numbers that add up to {targetSum1} --> {actual}")

    targetSum2 = 4
    expected = [1, 3]
    actual = findTwoNumberSum(arr, targetSum2)
    assert actual == expected
    print(f"Found the two numbers that add up to {targetSum2} --> {actual}")

    targetSumFail = 11
    expected = []
    actual = findTwoNumberSum(arr, targetSumFail)
    assert actual == expected
    print(f"Didn't find two numbers that add up to {targetSumFail} --> {actual}")