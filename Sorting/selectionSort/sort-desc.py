# Selection sort (descending)

# Input: int array, arr

# Time: O(n^2) -> iterate through arr n-1, n-2,..., 2, 1
#                 times = n(n-1)/2 times ~= O(n^2)
# Space: O(1)  -> stable in-place sort

from typing import List

def sort(arr: List[int]):
    for i in range(len(arr)):
        currMax = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[currMax]:
                currMax = j
        arr[currMax], arr[i] = arr[i], arr[currMax]

if __name__ == "__main__":
    arr = [9, 4, 6, 1, 5, 2, 7, 8, 3]
    sort(arr)
    assert arr == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Sweet. Selection-sorted the arr {arr}")

    allZeroesArr = [0, 0, 0, 0]
    sort(allZeroesArr)
    assert allZeroesArr == [0, 0, 0, 0]
    print(f"Sweet. Selection-sorted the arr {allZeroesArr}")

    alreadyDescArr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort(alreadyDescArr)
    assert alreadyDescArr == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Sweet. Selection-sorted the arr {alreadyDescArr}")