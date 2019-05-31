# Two number sum
# (return sorted array if can find target sum;
# empty array if cannot find target sum)

# Hash/dictionary approach
# Input: non-empty array with distinct integers arr,
# integer target sum targetSum

# Time: O(n)  -> iterate through each int in arr in
#                worst case before find sum
# Space: O(n) -> create new dictionary with n int in
#                worst case

from typing import List

def findTwoNumberSum(arr: List[int], targetSum: int):
    result = []
    numsDict = {}
    for num in arr:
        diff = targetSum - num
        if diff in numsDict:
            result.append(min(num, diff))
            result.append(max(num, diff))
            break
        else:
            numsDict[num] = True
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