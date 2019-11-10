# Relative sort array

# Time: O(nlogn) -> use Python sort function (Timsort)
# Space: O(n)    -> create array of len n (n = len of arr1) 

from typing import List

def relativeSortArray(arr1: List[int], arr2: List[int]):
    arr2Set = set(arr2)
    arr2Dict = dict()
    otherNums = []
        
    for n in arr1:
        if n in arr2Set:
            if n in arr2Dict:
                l = arr2Dict[n]
                l.append(n)
                arr2Dict[n] = l
            else:
                arr2Dict[n] = [n]
        else:
            otherNums.append(n)
            
    res = []
    for n in arr2:
        if n in arr2Dict:
            res.extend(arr2Dict[n])
        
    otherNums.sort()
    res.extend(otherNums)

    return res

if __name__ == "__main__":
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    expected = [2,2,2,1,4,3,3,9,6,7,19]
    actual = relativeSortArray(arr1, arr2)
    assert actual == expected
    print(f"Relatively sorted array {arr1}: {actual}")

    arr1 = [2, 7, 4, 3]
    arr2 = [4]
    expected = [4, 2, 3, 7]
    actual = relativeSortArray(arr1, arr2)
    assert actual == expected
    print(f"Relatively sorted array {arr1}: {actual}")