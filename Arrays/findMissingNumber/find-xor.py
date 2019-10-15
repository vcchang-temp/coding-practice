# Find missing number in array
# Array is of len n and elements are in range 1 to n+1

# XOR approach
# Time: O(n)  -> iterate through all elements in given array of len n
# Space: O(1) -> no extra space needed

from typing import List

def find(arr: List[int]):
    n = len(arr) + 1
    for i, num in enumerate(arr, start=1):
        n ^= i ^ num # a XOR a = 0 and a XOR 0 = a
    return n

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