# Sort a list with three unique numbers
# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
# Challenge: Try sorting the list using constant space.

# Input: non-empty array, arr, with at least 3 unique numbers

# Constant space approach
# Time: O(2n) ~ O(n) -> iterate through each int in arr
# Space: O(1)        -> in-place sort

from typing import List

def sort(arr: List[int]):
    pointer1 = 0
    count2s = 0
    count3s = 0

    for num in arr:
        if num == 1:
            arr[pointer1] = num
            pointer1 += 1
        elif num == 2:
            count2s += 1
        else:
            count3s += 1

    while count2s > 0:
        arr[pointer1] = 2
        count2s -= 1
        pointer1 += 1

    while count3s > 0:
        arr[pointer1] = 3
        count3s -= 1
        pointer1 += 1

    return arr

if __name__ == "__main__":
    arr = [3, 2, 3, 1, 1, 3, 2, 2, 1]
    expected = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    actual = sort(arr)
    assert actual == expected
    print(f"Wohoo, sorted three unique numbers: {actual}")