# Squares of a sorted array
# (return array with squares of given integers in
# sorted order)

# Input: array of integers in ascending order

# List comprehension + sort (short) approach
# Time: O(nlogn) -> sort() uses Timsort (hybrid of 
#                    merge, insertion sort)
# Space: O(n)    -> list comprehension creates new 
#                   list of len n of arr 

from typing import List

def sort(arr: List[int]):
    arr = [num**2 for num in arr]
    arr.sort()
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