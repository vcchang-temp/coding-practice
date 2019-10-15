# Find intersection of two arrays
# Assume inputs are not null and only count unique 
# number instances
# Return sorted array

# Time: O(nlogn) -> sorted uses Timsort which has a 
#                   runtime of O(nlogn)
# Space: O(n)    -> make two new sets that are at most
#                   of len n (n = len(arr1) + len(arr2)) 

from typing import List

def find(arr1: List[int], arr2: List[int]):
    arr1Set = set(arr1)
    intersection = set()
    for num in arr2:
        if num in arr1Set and num not in intersection:
            intersection.add(num)
    return sorted(intersection)

if __name__ == "__main__":
    arr1 = [1, 2, 5, 5, 8]
    arr2 = [5, 5, 6, 7]
    expected = [5]
    actual = find(arr1, arr2)
    assert actual == expected
    print(f"Intersection of arrays is: {actual} :)")

    arr1 = [2, 5, 0, 5, 8]
    arr2 = [1, 5, 6, 7, 0, 2]
    expected = [0, 2, 5]
    actual = find(arr1, arr2)
    assert actual == expected
    print(f"Intersection of arrays is: {actual} :)")

    arr1 = [1, 2, 5, 8]
    arr2 = [0, 2, 7, 8, 11]
    expected = [2, 8]
    actual = find(arr1, arr2)
    assert actual == expected
    print(f"Intersection of arrays is: {actual} :)")

    arr1 = []
    arr2 = [0, 2, 7, 8, 11]
    expected = []
    actual = find(arr1, arr2)
    assert actual == expected
    print(f"Intersection of arrays is: {actual} :)")