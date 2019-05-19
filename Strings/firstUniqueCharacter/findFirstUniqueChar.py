# Find first unique character
# (return index of first unique char)

# Input: string s

# Brute force approach (compare char with every other char that comes after)

# Time: O(n^2) -> check every char with all chars in chars that come after 
#                 current char
# Space: O(1)  -> space remains constant

def findFirstUniqueChar(s: str):
    if s == None:
        return -1

    if len(s) == 1:
        return 0

    alreadySeenChars = []
    for i in range(len(s)):
        uniqueIdx = findFirstUniqueHelper(i, s, alreadySeenChars)
        if uniqueIdx != None:
            return uniqueIdx
        if s[i] not in alreadySeenChars:
            alreadySeenChars.append(s[i])
    else:
        return -1

def findFirstUniqueHelper(currUniqueIdx: int, s: str, alreadySeenChars: list):
    for j in range(currUniqueIdx+1, len(s)):
        if s[currUniqueIdx] == s[j]:
            break
        if j == len(s) - 1 and s[currUniqueIdx] not in alreadySeenChars:
            return currUniqueIdx
        if j == len(s) - 1 and currUniqueIdx == len(s) - 2:
            if s[currUniqueIdx] not in alreadySeenChars:
                return currUniqueIdx
            elif s[j] not in alreadySeenChars:
                return j

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