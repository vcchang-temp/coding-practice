# Find missing number in array
# Array is of len n and elements are in range 1 to n+1

# Sum of series formula approach
# Time: O(n)  -> sum() time complexity is likely O(n)
# Space: O(1) -> no extra space needed

from typing import List

def find(arr: List[int]):
    n = len(arr) + 1
    seriesSum = (n*(n+1))//2 # sum of numbers from 1 to n; // discards remainder and gives integer
    arrSum = sum(arr)
    return seriesSum - arrSum

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