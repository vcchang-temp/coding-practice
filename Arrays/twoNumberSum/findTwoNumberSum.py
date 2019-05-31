# Two number sum
# (return sorted array if can find target sum;
# empty array if cannot find target sum)

# Sorting + brute force approach
# Input: non-empty array with distinct integers arr,
# integer target sum targetSum

# Time: O(n^2) -> sorting --> O(nlogn) < O(n^2) of
#                 two nested for loops
# Space: O(1)  -> results array of len 2

from typing import List

def findTwoNumberSum(arr: List[int], targetSum: int):
    arr.sort()
    result = []
    for i in range(len(arr)):
        diff = targetSum - arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] == diff:
                result.append(arr[i])
                result.append(arr[j])
                break
        if result:
            break
    return result

if __name__ == "__main__":
    arr = [3, 2, 7, -4, 1, 0, -1, 6]
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