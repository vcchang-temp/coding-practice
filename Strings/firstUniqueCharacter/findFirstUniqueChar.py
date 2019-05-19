# Find first unique character
# (return index of first unique char)

# Input: string s

# Dictionary approach

# Time: O(n)  -> check every char in s of len n
# Space: O(n) -> create new dictionary with n keys

def findFirstUniqueChar(s: str):
    if s == None:
        return -1

    chars = {}
    for i in range(len(s)):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1

    for i in range(len(s)):
        if chars[s[i]] == 1:
            return i
    else:
        return -1

if __name__ == "__main__":
    uniqueCharS = "main course, mmmm"
    expected = 1
    actual = findFirstUniqueChar(uniqueCharS)
    assert actual == expected
    print(f"Found unique character at index {actual} of {uniqueCharS}")

    noUniqueCharS = "mmmmmooo"
    expected = -1
    actual = findFirstUniqueChar(noUniqueCharS)
    assert actual == expected
    print(f"Did not fing unique character in {noUniqueCharS}")