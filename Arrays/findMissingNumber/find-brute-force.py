# WIP

# Find missing number in array
# Array is of len n and elements are in range 1 to n+1

# Brute force (looping) approach
# Time: O(n^2) -> loop through array of len n for each element
# Space: O(1)  -> space does not grow with input

from typing import List

def find(arr: List[int]):
    currNum = 1
    haveSeenLastNum = False
    for j in range(len(arr)):
        if currNum == arr[j]:
            currNum += 1
            if arr[j] == len(arr) + 1:
                haveSeenLastNum = True
            continue
        elif j == len(arr)-1 and not haveSeenLastNum:
            return currNum + 1
        for i in range(len(arr)):
            if currNum == arr[i]:
                currNum += 1
                if arr[j] == len(arr) + 1:
                    haveSeenLastNum = True
                break
            elif i == len(arr) - 1:
                return currNum

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