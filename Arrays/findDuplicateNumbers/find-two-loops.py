# Find the duplicate numbers in integer array
# Do not add numbers more than once even if they
# appear in the array more than twice
# Return stable result

# Two loops approach
# Time: O(n^2) -> 1st loop: iterate through given array with n elements
#                 2nd loop: iterate through n-1, n-2,..., 2, 1 elements
#                           = arithmetic series 1, 2,..., n-2, n-1
#                           = n(n-1)/2
#                 altogether: O(n + n(n-1)/2) ~= O(n^2)
# Space: O(n) -> store at most n/2 elements in new array ~= O(n)

from typing import List

def findDupes(nums: List[int]):
    dupes = []
    for i in range(len(nums)):
        j = i + 1
        for j in range(j, len(nums)):
            if nums[i] == nums[j] and nums[i] not in dupes: # O(n) runtime for in operation
                dupes.append(nums[i])
    return dupes

if __name__ == "__main__":
    arr = [1, 3, 6, 3, 2, 7, 1]
    expected = [1, 3]
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