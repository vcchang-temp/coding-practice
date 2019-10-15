# Find missing number in array
# Array is of len n and elements are in range 1 to n+1

# Sort first approach
# Time: O(nlogn) -> sorting takes up most time; Python
#                   uses Timsort which has a runtime of
#                   O(nlogn)
# Space: O(1)  -> space does not grow with input

from typing import List

def find(arr: List[int]):
    arr.sort()
    currNum = 1
    for num in arr:
        if currNum == 1 and num != 1: # edge case of first num missing
            return 1
        elif currNum == len(arr) and num < len(arr)+1: # edge case of last num missing
            return currNum+1

        if num == currNum:
            currNum += 1
            continue
        elif num > currNum:
            return currNum
        currNum += 1

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