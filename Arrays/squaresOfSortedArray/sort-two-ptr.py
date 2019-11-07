# Squares of a sorted array
# (return array with squares of given integers in
# sorted order)

# Input: array of integers in ascending order

# Two-pointer approach
# Time: O(n)  -> visit each element of array of len n at most twice
# Space: O(n) -> create new array holding n numbers

from typing import List

def sort(A: List[int]):
    i = findIdxOfLastNegNum(A)
    j = i + 1
    res = []

    while i >= 0 and j < len(A):
        if A[i]**2 <= A[j]**2:
            res.append(A[i]**2)
            i -= 1
        else:
            res.append(A[j]**2)
            j += 1
    
    while i >= 0:
        res.append(A[i]**2)
        i -= 1

    while j < len(A):
        res.append(A[j]**2)
        j += 1
    
    return res

def findIdxOfLastNegNum(A: List[int]):
    i = 0
    for num in A:
        if num < 0:
            i += 1
        if num >= 0:
            break
    return i

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