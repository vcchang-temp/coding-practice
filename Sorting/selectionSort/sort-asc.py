# Selection sort (ascending)

# Input: int array, arr

# Time: O(n^2) -> iterate through arr n-1, n-2,..., 2, 1
#                 times = n(n-1)/2 times ~= O(n^2)
# Space: O(1)  -> stable in-place sort

from typing import List

def sort(arr: List[int]):
    for i in range(len(arr)):
        currMin = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[currMin]:
                currMin = j
        arr[currMin], arr[i] = arr[i], arr[currMin]

if __name__ == "__main__":
    arr = [9, 4, 6, 1, 5, 2, 7, 8, 3]
    sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Sweet. Selection-sorted the arr {arr}")

    allZeroesArr = [0, 0, 0, 0]
    sort(allZeroesArr)
    assert allZeroesArr == [0, 0, 0, 0]
    print(f"Sweet. Selection-sorted the arr {allZeroesArr}")

    alreadyAscArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sort(alreadyAscArr)
    assert alreadyAscArr == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Sweet. Selection-sorted the arr {alreadyAscArr}")