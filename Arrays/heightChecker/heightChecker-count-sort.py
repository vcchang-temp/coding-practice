# Height checker

# Bucket/count sort approach
# Time: O(n)  -> make array of 101 elements ~= n if heights has len n
# Space: O(n) -> made array of 101 elements ~= n if heights has len n

from typing import List

def heightChecker(heights: List[int]):
    heightsMap = [None] * 101
    for h in heights: # store num occurrences of each h at idx representing h
        heightsMap[h] = heightsMap[h] + 1 if heightsMap[h] else 1
        
    ans = 0
    hCurr = 1 # start at h = 1
    for h in heights:
        while not heightsMap[hCurr]:
            hCurr += 1
    
        if hCurr != h:
            ans += 1
        heightsMap[hCurr] -= 1
    return ans

if __name__ == "__main__":
    heights = [1, 1, 4, 3, 6, 7]
    expected = 2
    actual = heightChecker(heights)
    assert actual == expected
    print(f"There are {actual} students that are in the wrong position for non-decreasing-height order in {heights}")