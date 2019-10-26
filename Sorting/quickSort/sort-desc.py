# Quicksort - in-place, stable algorithm
# (descending version)

# Time: O(nlogn) (avg) -> break array into half until only one element in each subarray.
#                         *If* we can break array into roughly two equal halves each time,
#                         then we can do this logn (base 2) times, creating logn levels.
#                         For each level, visit each element once. 
#                         Therefore, n * logn -> O(nlogn) runtime
# O(n^2) (worst-case)  -> if we don't break array into roughly equal halves each time, 
#                         but where first half has n-1 and second half has 1 element,
#                         then this means we'll create n levels. 
#                         For each level, we'll visit each element once.
#                         Therefore, n * n -> O(n^2) runtime
# Space: O(1)          -> in-place sorting algorithm

from typing import List

def quicksort(arr: List):
    return _quicksort(arr, 0, len(arr)-1)

def _quicksort(arr: List, start: int, end: int):
    if start >= end:
        return
    
    p = partition(arr, start, end)
    _quicksort(arr, start, p-1)
    _quicksort(arr, p+1, end)

def partition(arr: List, start: int, end: int):
    follower = leader = start
    while leader < end:
        if arr[leader] >= arr[end]: # pick end == pivot; should be = to be stable sort
            arr[leader], arr[follower] = arr[follower], arr[leader] # building left subarray of elements larger than pivot
            follower += 1
        leader += 1
    arr[follower], arr[end] = arr[end], arr[follower]
    return follower

if __name__ == "__main__":
    arr = [1, 6, 2, 5, 3, 0, 5, 7, 8]
    quicksort(arr)
    assert arr == [8, 7, 6, 5, 5, 3, 2, 1, 0]
    print(f"Wow [1, 6, 2, 5, 3, 0, 5, 7, 8] was quickly sorted: {arr}")

    arr = []
    quicksort(arr)
    assert arr == []
    print(f"Wow [] was quickly sorted: {arr}")

    arr = [1]
    quicksort(arr)
    assert arr == [1]
    print(f"Wow [] was quickly sorted: {arr}")

    arr = ["a", "f", "c", "v", "k", "s", "d", "g"]
    quicksort(arr)
    assert arr == ['v', 's', 'k', 'g', 'f', 'd', 'c', 'a']
    print(f"Wow ['a', 'f', 'c', 'v', 'k', 's', 'd', 'g'] was quickly sorted: {arr}")