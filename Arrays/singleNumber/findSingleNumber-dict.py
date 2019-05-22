# Single number

# Input: non-empty array, arr, with integers where 
# there's only one integer that appears once and all 
# others appear twice

# Dictionary approach
# Time: O(n)  -> iterate through each int in arr
# Space: O(n) -> create dictionary with at most n-1
#                ints 

from typing import List

def findSingleNumber(arr: List[int]):
    arrDict = {}
    for num in arr:
        if num in arrDict:
            arrDict[num] += 1
        else:
            arrDict[num] = 1
    return min(arrDict, key=arrDict.get)

if __name__ == "__main__":
    arr = [2, 3, 2, 3, 7, 8, 7]
    expected = 8
    actual = findSingleNumber(arr)
    assert actual == expected
    print(f"Wootttt found the single number ;), lucky number {actual}")