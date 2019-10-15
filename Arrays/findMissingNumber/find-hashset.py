# Find missing number in array
# Array is of len n and elements are in range 1 to n+1

# Hashset approach
# Time: O(n)  -> iterate through set with n keys (from array of len n)
# Space: O(n) -> create set with n elements

from typing import List

def find(arr: List[int]):
    arrSet = set(arr)
    n = len(arr) + 1
    for i in range(1, n+1):
        if i not in arrSet:
            return i

if __name__ == "__main__":
    arr = [1, 4, 5, 8, 2, 3, 6]
    expected = 7
    actual = find(arr)
    assert actual == expected
    print(f"Awesome, we found the missing number {actual}!")

    arr = [1, 2, 4]
    expected = 3
    actual = find(arr)
    assert actual == expected
    print(f"Awesome, we found the missing number {actual}!")

    arr = [2]
    expected = 1
    actual = find(arr)
    assert actual == expected
    print(f"Awesome, we found the missing number {actual}!")

    arr = [1]
    expected = 2
    actual = find(arr)
    assert actual == expected
    print(f"Awesome, we found the missing number {actual}!")

    arr = [3, 1, 4]
    expected = 2
    actual = find(arr)
    assert actual == expected
    print(f"Awesome, we found the missing number {actual}!")