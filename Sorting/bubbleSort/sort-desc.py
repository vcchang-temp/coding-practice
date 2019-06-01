# Bubble sort (descending)

# Input: int array, arr

# Time: O(n^2) -> traverse arr n, n-1, n-2,... n-n+1
#                 times = n(n-1)/2 times = O(n^2)
# Space: O(1)  -> in-place sort, stable

from typing import List

def sort(arr: List[int]):
    back = len(arr)-1

    while back > 0:
        for i in range(back):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        back -= 1

if __name__ == "__main__":
    arr = [9, 4, 6, 1, 5, 2, 7, 8, 3]
    sort(arr)
    assert arr == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"WOoOoOooOO bubble-sOrted the arr {arr}")

    allZeroesArr = [0, 0, 0, 0]
    sort(allZeroesArr)
    assert allZeroesArr == [0, 0, 0, 0]
    print(f"WOoOoOooOO bubble-sOrted the arr {allZeroesArr}")

    alreadyAscArr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort(alreadyAscArr)
    assert alreadyAscArr == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"WOoOoOooOO bubble-sOrted the arr {alreadyAscArr}")