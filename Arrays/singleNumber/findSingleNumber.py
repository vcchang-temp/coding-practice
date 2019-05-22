# Single number

# Input: non-empty array, arr, with integers where 
# there's only one integer that appears once and all 
# others appear twice

# Set approach
# Time: O(n)  -> iterate through each int in arr
# Space: O(n) -> create set with at most n/2 ints 

from typing import List

def findSingleNumber(arr: List[int]):
    numSet = set()

    for num in arr:
        if num not in numSet:
            numSet.add(num)
        else:
            numSet.remove(num)
    
    return numSet.pop()

if __name__ == "__main__":
    arr = [2, 3, 2, 3, 7, 8, 7]
    expected = 8
    actual = findSingleNumber(arr)
    assert actual == expected
    print(f"Wootttt found the single number ;), lucky number {actual}")