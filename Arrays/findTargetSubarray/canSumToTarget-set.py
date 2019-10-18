# Determine if array contains a subarray that sums up to target

# Set/memory approach
# Time: O(n)  -> iterate through every int in given array of len n
# Space: O(n) -> store at most n ints in hashset

from typing import List

def canSumTo(target: int, arr: List):
    if not arr: # empty or null array
        return False
    
    runningTotal = 0
    currentSums = set()
    for num in arr:
        runningTotal += num

        if runningTotal == target: # case 1: all nums seen sum up to target
            return True

        if runningTotal not in currentSums: # store largest subarray seen so far
            currentSums.add(runningTotal)

        intermediateSum = runningTotal - target # case 2: intermediateSum == subarray total
        if intermediateSum in currentSums:      # that remains after target has been subtracted
            return True                         # from the largest subarray total seen so far
    return False

if __name__ == "__main__":
    arr = [4, 2, -1, 3, 5, 6]
    target = 6
    expected = True
    actual = canSumTo(target, arr)
    assert actual == expected
    print(f"Woohoo, {arr} contains target {target}!")

    arr = [2, -1, 3, 5, 6]
    target = 4
    expected = True
    actual = canSumTo(target, arr)
    assert actual == expected
    print(f"Woohoo, {arr} contains target {target}!")

    arr = [4, 2, -1, 3, 5, 6]
    target = 12
    expected = False
    actual = canSumTo(target, arr)
    assert actual == expected
    print(f"O noes, {arr} does not contain target {target}")