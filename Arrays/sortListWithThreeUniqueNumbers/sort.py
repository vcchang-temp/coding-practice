# Sort a list with three unique numbers
# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
# Challenge: Try sorting the list using constant space.

# Input: non-empty array, arr, with at least 3 unique numbers

# Three-array approach
# Time: O(n)  -> iterate through each int in arr
# Space: O(n) -> create three arrays with a total length of n (arr length) 

from typing import List

def sort(arr: List[int]):
    arr1 = []
    arr2 = []
    arr3 = []

    for num in arr:
        if num == 1:
            arr1.append(num)
        elif num == 2:
            arr2.append(num)
        else:
            arr3.append(num)
    
    arr1.extend(arr2)
    arr1.extend(arr3)
    return arr1

if __name__ == "__main__":
    arr = [3, 2, 3, 1, 1, 3, 2, 2, 1]
    expected = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    actual = sort(arr)
    assert actual == expected
    print(f"Wohoo, sorted three unique numbers: {actual}")