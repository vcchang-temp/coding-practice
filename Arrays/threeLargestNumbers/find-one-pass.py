# Three largest numbers
# (return sorted array of three largest numbers)

# Input: int array, arr

# One pass approach
# Time: O(n)  -> iterate through arr once
# Space: O(1) -> create array of three nums and
#                not O(n) because created array
#                does not grow with input

from typing import List

def find(arr: List[int]):
    maxNums = [None, None, None]
    for i in range(len(arr)):
        if not maxNums[2]:
            maxNums[2] = arr[i]
            continue
        elif not maxNums[1]:
            if arr[i] > maxNums[2]:
                maxNums[1], maxNums[2] = maxNums[2], arr[1]
            else:
                maxNums[1] = arr[i]
            continue
        elif not maxNums[0] or None not in maxNums:
            if arr[i] > maxNums[2]:
                maxNums[0], maxNums[1], maxNums[2] = maxNums[1], maxNums[2], arr[i]
            elif arr[i] > maxNums[1]:
                maxNums[0], maxNums[1] = maxNums[1], arr[i]
            elif arr[i] > maxNums[0]:
                maxNums[0] = arr[i]
    return maxNums

if __name__ == "__main__":
    arr = [18, 1, 30, 42, 57, 8, 9, 26]
    expected = [30, 42, 57]
    actual = find(arr)
    assert actual == expected
    print(f"And the three largest numbers in {arr} are... {actual}!")

    arrWithDupes = [17, 5, 17, 1, 17]
    expectedDupes = [17, 17, 17]
    actualDupes = find(arrWithDupes)
    assert actualDupes == expectedDupes
    print(f"And the three largest numbers in {arr} are... {actualDupes}!")