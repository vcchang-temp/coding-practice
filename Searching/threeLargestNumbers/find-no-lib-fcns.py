# Three largest numbers
# (return sorted array of three largest numbers)

# Input: int array, arr

# Brute force approach (without using library functions
# like max, sort, remove, insert)
# Time: O(n)  -> iterate through arr three times ->
#                O(3*n) ~= O(n)
# Space: O(1) -> create array of three nums and
#                not O(n) because created array
#                does not grow with input

from typing import List

def find(arr: List[int]):
    idxs = findThreeLargestNumIdxs(arr)
    return [arr[idxs[0]], arr[idxs[1]], arr[idxs[2]]]

def findThreeLargestNumIdxs(arr: List[int]):
    idxs = []
    firstLargestNumIdx = findLargestNumIdx(arr, idxs)
    idxs.append(firstLargestNumIdx)
    secondLargestNumIdx = findLargestNumIdx(arr, idxs)
    idxs.append(secondLargestNumIdx)
    thirdLargestNumIdx = findLargestNumIdx(arr, idxs)
    return [thirdLargestNumIdx, secondLargestNumIdx, firstLargestNumIdx]

def findLargestNumIdx(arr: List[int], idxs: List[int]):
    maxNumIdx = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[maxNumIdx] and i not in idxs:
            maxNumIdx = i
    return maxNumIdx

if __name__ == "__main__":
    arr = [17, 90, 34, 52, 67, 1, 0, 903]
    expected = [67, 90, 903]
    actual = find(arr)
    assert actual == expected
    print(f"Found the three largest numbers in the array! {actual}")

    arrWithDupes = [17, 5, 17, 1, 903]
    expectedDupes = [17, 17, 903]
    actualDupes = find(arrWithDupes)
    assert actualDupes == expectedDupes
    print(f"Found the three largest numbers in the array! {actualDupes}")