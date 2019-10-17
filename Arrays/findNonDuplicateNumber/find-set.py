# Find non-duplicate element in array with duplicates
# Assume at most two of the same element in array

# Set approach
# Time: O(n)  -> iterate through every element in given array of len n
# Space: O(n) -> create new set of at most size n/2 ~= O(n)

from typing import List

def find(arr: List):
    arrSet = set()
    for elem in arr:
        if elem not in arrSet:
            arrSet.add(elem)
        else:
            arrSet.remove(elem)
    return arrSet.pop()

if __name__ == "__main__":
    arr = [1, 1, 4, 5, 3, 9, 5, 9, 4]
    expected = 3
    actual = find(arr)
    assert actual == expected
    print(f"Found the non-duplicate element: {actual}")

    arr = [1, 1, 'bah', 'a', 'yes!', 9, 'a', 9, 'bah']
    expected = 'yes!'
    actual = find(arr)
    assert actual == expected
    print(f"Found the non-duplicate element: {actual}")