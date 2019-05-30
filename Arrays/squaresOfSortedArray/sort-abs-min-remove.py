# Squares of a sorted array
# (return array with squares of given integers in
# sorted order)

# Input: array of integers in ascending order

# Absolute + find min + remove approach
# Time: O(n^2) -> loop takes up most time;
#                 find min for each int in arr of len n +
#                 remove min from arr of len n -> O(n*(n+n)) 
#                 ~= O(n^2)
# Space: O(n)    -> list comprehension creates new 
#                   list of len n of arr

from typing import List

def sort(arr: List[int]):
    srtSqrArr = []
    arr = [abs(num) for num in arr]
    while len(arr) > 0:
        minNum = min(arr)
        srtSqrArr.append(minNum ** 2)
        arr.remove(minNum)
    return srtSqrArr

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