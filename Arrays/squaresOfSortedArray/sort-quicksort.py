# Squares of a sorted array
# (return array with squares of given integers in
# sorted order)

# Input: array of integers in ascending order

# List comprehension + sort (short) approach
# Time: O(nlogn) -> quicksort divides array in half logn times and
#                   visits each element once in arrays at each level
#                   -> n visits * logn levels
# Space: O(1)    -> square and sort in-place

from typing import List

def sort(A: List[int]):
    # A = [num**2 for num in A] # more concise but less space-efficient
    for i, num in enumerate(A):
        A[i] = num **2
    quicksort(A)
    return A
    
def quicksort(A: List[int]):
    return _quicksort(A, 0, len(A)-1)
    
def _quicksort(A: List[int], start: int, end: int):
    if start >= end:
        return
        
    p = partition(A, start, end)
    _quicksort(A, start, p-1)
    _quicksort(A, p+1, end)
    
def partition(A: List[int], start: int, end: int):
    follower = leader = start
    while leader < end:
        if A[leader] <= A[end]:
            A[leader], A[follower] = A[follower], A[leader]
            follower += 1
        leader += 1
    A[follower], A[end] = A[end], A[follower]
    return follower

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