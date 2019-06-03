# Three largest numbers
# (return sorted array of three largest numbers)

# Input: int array, arr

# Brute force approach (without using library functions
# like max and sort)
# Time: O(n)  -> iterate through arr three times ->
#                O(3*n) ~= O(n)
# Space: O(n) -> create array of three nums -> O(n)
#                in cases when n <= 3; otherwise more
#                like O(1)

from typing import List

def find(arr: List[int]):
    largestNums = []

    firstLargestNum = findLargestNum(arr)
    largestNums.insert(0, firstLargestNum)
    arr.remove(firstLargestNum)

    secondLargestNum = findLargestNum(arr)
    largestNums.insert(0, secondLargestNum)
    arr.remove(secondLargestNum)

    thirdLargestNum = findLargestNum(arr)
    largestNums.insert(0, thirdLargestNum)
    # technically no need to remove third largest num

    return largestNums

def findLargestNum(arr: List[int]):
    maxNum = arr[0]
    for num in arr:
        if num > maxNum:
            maxNum = num
    return maxNum

if __name__ == "__main__":
    arr = [17, 90, 34, 52, 67, 1, 0, 903]
    expected = [67, 90, 903]
    actual = find(arr)
    assert actual == expected
    print(f"Found the three largest numbers in the array! {actual}")

    arrWithDupes = [17, 5, 17, 1, 903]
    expectedDupes = [17, 17, 903]
    actualDupes = find(arrWithDupes)
    assert actualDupes == expectedDupes
    print(f"Found the three largest numbers in the array! {actualDupes}")