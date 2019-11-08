# Peak Index in a Mountain Array

# Assume there's guaranteed to be a mountain and array is of at least len 3

# Time: O(n)  -> iterate through at least n/2 numbers in array of len n
# Space: O(1) -> input doesn't affect space used

from typing import List

def peakIndexInMountainArray(A: List[int]):
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            return i-1

if __name__ == "__main__":
    arr = [0, 12, 3]
    expected = 1
    actual = peakIndexInMountainArray(arr)
    assert actual == expected
    print(f"Found peak of mountain {arr}: {actual}")

    arr = [0, 1, 3, 1, 0]
    expected = 2
    actual = peakIndexInMountainArray(arr)
    assert actual == expected
    print(f"Found peak of mountain {arr}: {actual}")