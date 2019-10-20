# Unique number of occurrences

# Two-liner using same data structures as areUnique.py solution
# Time: O(n)  -> iterate through each number in array of len n
# Space: O(n) -> create dictionary (2n) and set (n) = O(2n + n)
#                = O(3n) ~= O(n)

from typing import List
from collections import Counter

def uniqueOccurrences(arr: List[int]):
    dict = Counter(arr)
    return len(dict.values()) == len(set(dict.values()))

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