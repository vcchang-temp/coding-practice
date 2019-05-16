# Reverse string

# Input: List[str]

# Time: O(n) -> going through n/2 characters (list len = n) = O(n/2) ~= O(n)
# Space: O(1) -> using given list space to create reversed string

from typing import List

def reverse(s: List[str]):
    if not s:
        return ""
    
    front = 0
    back = len(s)-1

    while front < back:
        s[front], s[back] = s[back], s[front]
        front += 1
        back -= 1

    return s    # only returning for test purpose

if __name__ == '__main__':
    expected = ["g", "n", "i", "r", "t", "s"]
    actual = reverse(["s", "t", "r", "i", "n", "g"])
    assert actual == expected
    print("Yes, string reversed!")