# Find first unique character
# (return index of first unique char)

# Input: string s

# Ascii array approach

# Time: O(n)  -> check every char in s of len n
# Space: O(n) -> create new array of len n

def findFirstUniqueChar(s: str):
    cArr = [0] * 26
    for c in s:
        normalizedIdx = ord(c)-97
        cArr[normalizedIdx] = 1 if not cArr[normalizedIdx] else cArr[normalizedIdx] + 1
    for i, c in enumerate(s):
        if cArr[ord(c)-97] == 1:
            return i
    else:
        return -1

if __name__ == "__main__":
    uniqueCharS = "main course, mmmm"
    expectedUnique = 1
    actualUnique = findFirstUniqueChar(uniqueCharS)
    assert actualUnique == expectedUnique
    print(f"Found unique character at index {actualUnique} of {uniqueCharS}")

    uniqueCharS2 = "leetcode"
    expectedUnique2 = 0
    actualUnique2 = findFirstUniqueChar(uniqueCharS2)
    assert actualUnique2 == expectedUnique2
    print(f"Found unique character at index {actualUnique2} of {uniqueCharS2}")

    uniqueCharS3 = "v"
    expectedUnique3 = 0
    actualUnique3 = findFirstUniqueChar(uniqueCharS3)
    assert actualUnique3 == expectedUnique3
    print(f"Found unique character at index {actualUnique3} of {uniqueCharS3}")

    uniqueCharS4 = "vdddffggva"
    expectedUnique4 = 9
    actualUnique4 = findFirstUniqueChar(uniqueCharS4)
    assert actualUnique4 == expectedUnique4
    print(f"Found unique character at index {actualUnique4} of {uniqueCharS4}")

    noUniqueCharS = "mmmmmooo"
    expectedNoUnique = -1
    actualNoUnique = findFirstUniqueChar(noUniqueCharS)
    assert actualNoUnique == expectedNoUnique
    print(f"Did not find unique character in {noUniqueCharS}")

    noUniqueCharS2 = "daddad"
    expectedNoUnique2 = -1
    actualNoUnique2 = findFirstUniqueChar(noUniqueCharS2)
    assert actualNoUnique2 == expectedNoUnique2
    print(f"Did not find unique character in {noUniqueCharS2}")