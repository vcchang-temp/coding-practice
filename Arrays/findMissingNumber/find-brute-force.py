# Find missing number in array
# Array is of len n and elements are in range 1 to n+1

# Brute force (looping) approach
# Time: O(n^2) -> worst case: reversed order -> n-1, n-2,..., 1
#                 elements to iterate through for each loop iteration
#                 = n(n-1)/2 ~= O(n^2)
# Space: O(1)  -> space does not grow with input

from typing import List

def find(arr: List[int]):
    currNum = 1
    for i in range(len(arr)):
        if currNum == arr[i]:
            currNum += 1
            continue
        elif i == len(arr)-1:
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