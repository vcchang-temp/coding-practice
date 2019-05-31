# Two number sum
# (return sorted array if can find target sum;
# empty array if cannot find target sum)

# Sorting + two pointers approach
# Input: non-empty array with distinct integers arr,
# integer target sum targetSum

# Time: O(nlogn) -> Python uses Timsort -> O(nlogn)
# Space: O(1)    -> no extra space needed

from typing import List

def findTwoNumberSum(arr: List[int], targetSum: int):
    arr.sort()
    front = 0
    back = len(arr)-1

    while front != back:
        sum = arr[front] + arr[back]
        if sum == targetSum:
            return [min(arr[front], arr[back]), max(arr[front], arr[back])]
        elif sum > targetSum:
            back -= 1
        else:
            front += 1
    else:
        return []

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

    arr2 = [2, 3, 4]
    targetSum = 6
    expected = [2, 4]
    actual = findTwoNumberSum(arr2, targetSum)
    assert actual == expected
    print(f"Found the two numbers that add up to {targetSum} --> {actual}")

    targetSumFail = 11
    expected = []
    actual = findTwoNumberSum(arr, targetSumFail)
    assert actual == expected
    print(f"Didn't find two numbers that add up to {targetSumFail} --> {actual}")