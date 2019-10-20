# Unique number of occurrences

# Time: O(n)  -> iterate through each number in array of len n
# Space: O(n) -> create dictionary (2n) and set (n) = O(2n + n)
#                = O(3n) ~= O(n)

from typing import List

def uniqueOccurrences(arr: List[int]):
    dict = {}
    for num in arr:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    uniqueCount = set()
    for occurrences in dict.values():
        if occurrences not in uniqueCount:
            uniqueCount.add(occurrences)
        else:
            return False
    return True

if __name__ == "__main__":
    arr = [1, 2, 2, 1, 1, 3]
    expected = True
    actual = uniqueOccurrences(arr)
    assert actual == expected
    print(f"Found unique number of value occurrences in {arr}!")

    arr = [1, 2, 2, 1, 3]
    expected = False
    actual = uniqueOccurrences(arr)
    assert actual == expected
    print(f"Found unique number of value occurrences in {arr}!")