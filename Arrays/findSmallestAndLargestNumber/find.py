# Find smallest and largest numbers in unsorted array
# Assume inputs are not null
# Return sorted array

# Time: O(n)  -> iterate through every element in given array of len n
# Space: O(1) -> return list with only two elements ~= O(1) (output doesn't grow with input)

from typing import List

def find(arr: List[int]):
    if not arr:
        return []

    smallestSoFar, largestSoFar = arr[0], arr[0]
    for num in arr:
        if num < smallestSoFar:
            smallestSoFar = num
        if num > largestSoFar:
            largestSoFar = num
    return [smallestSoFar, largestSoFar]

if __name__ == "__main__":
    arr = [4, 58, 12, 67, 21, 78, 0, 12]
    expected = [0, 78]
    actual = find(arr)
    assert actual == expected
    print(f"Yay found the smallest and largest numbers in array: {actual}")

    arr = [4, 58, 121, 67, 21, 4, 12]
    expected = [4, 121]
    actual = find(arr)
    assert actual == expected
    print(f"Yay found the smallest and largest numbers in array: {actual}")

    arr = [123, 123, 123]
    expected = [123, 123]
    actual = find(arr)
    assert actual == expected
    print(f"Yay found the smallest and largest numbers in array: {actual}")

    arr = []
    expected = []
    actual = find(arr)
    assert actual == expected
    print(f"Yay found the smallest and largest numbers in array: {actual}")