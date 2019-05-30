# Squares of a sorted array
# (return array with squares of given integers in
# sorted order)

# Input: array of integers in ascending order

# Find-min sort approach
# Time: O(n^2) -> (n-2) passes (inner for loop) 
#                 through (n-1) ints (+1 extra 
#                 check in terminating outer for
#                 loop) -> O((n-2)(n)) ~= O(n^2) 
# Space: O(1)  -> modifying arr in-place

from typing import List

def sort(arr: List[int]):
    for i in range(len(arr)):
        arr[i] = arr[i] ** 2
    for i in range(len(arr)):
        lowestNumIdxSoFar = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowestNumIdxSoFar]:
                lowestNumIdxSoFar = j
        arr[i], arr[lowestNumIdxSoFar] = arr[lowestNumIdxSoFar], arr[i]
    return arr

if __name__ == "__main__":
    arr = [-3, -2, 1, 3, 5]
    expected = [1, 4, 9, 9, 25]
    actual = sort(arr)
    assert actual == expected
    print(f"Successfully squared {arr} into {actual}")

    arrZero = [0]
    expectedZero = [0]
    actualZero = sort(arrZero)
    assert actualZero == expectedZero
    print(f"Successfully squared {arrZero} into {actualZero}")

    arrZeroOne = [0, 1]
    expectedZeroOne = [0, 1]
    actualZeroOne = sort(arrZeroOne)
    assert actualZeroOne == expectedZeroOne
    print(f"Successfully squared {arrZeroOne} into {actualZeroOne}")