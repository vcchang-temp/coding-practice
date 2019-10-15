# Find the duplicate numbers in integer array
# Return stable result

# Set approach
# Time: O(n)  -> iterate through every element in given array
# Space: O(n) -> store in set at most all elements in given array of len n

from typing import List

def findDupes(nums: List[int]):
    dupes = []
    noDupes = set()

    for num in nums:
        if num not in noDupes: # O(1) for in operation
            noDupes.add(num)
        else:
            dupes.append(num)
    return dupes

if __name__ == "__main__":
    arr = [1, 3, 6, 3, 2, 7, 1]
    expected = [3, 1]
    actual = findDupes(arr)
    assert actual == expected
    print(f"Wahoo found the duplicate numbers: {actual}")

    emptyArr = []
    expected = []
    actual = findDupes(emptyArr)
    assert actual == expected
    print(f"Wahoo found the duplicate numbers: {actual}")

    allUniqueArr = [1, 3, 6, 2, 7]
    expected = []
    actual = findDupes(allUniqueArr)
    assert actual == expected
    print(f"Wahoo found the duplicate numbers: {actual}")