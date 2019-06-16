# String compression
# (length of compression must always be smaller
# than or equal to the original array)

# Input: array of char (strings) chars

# In-place approach
# Time: O(n)  -> iterate through each char of chars 
#                of len n
# Space: O(1) -> in-place so no extra space needed

from typing import List

def compress(chars: List[str]):
    if not chars or len(chars) == 1:
        return len(chars)
    currCharIdx = 0
    currCharRunnerIdx = 0
    charCount = 0
    currIdx = 0
    while currCharRunnerIdx < len(chars):
        while chars[currCharRunnerIdx] == chars[currCharIdx]:
            charCount += 1
        if charCount == 1:
            chars[currIdx] = chars[currCharIdx]
            charCount = 0
            currIdx += 1
        else:
            chars[currIdx] = chars[currCharIdx]
            chars[currIdx + 1] = charCount
            charCount = 0
            currIdx += 2
    result = chars[:currIdx + 1]
    return len(result)

if __name__ == "__main__":
    charsEmpty = []
    # expectedEmpty = []
    expectedEmpty = 0
    actualEmpty = compress(charsEmpty)
    assert actualEmpty == expectedEmpty
    print(f"Yes! Compressed {charsEmpty} to array of len {actualEmpty}")

    charsOne = ["a"]
    # expectedOne = ["a"]
    expectedOne = 1
    actualOne = compress(charsOne)
    assert actualOne == expectedOne
    print(f"Yes! Compressed {charsOne} to array of len {actualOne}")
    
    charsSimple = ["a", "b"]
    # expectedSimple = ["a", "b"]
    expectedSimple = 2
    actualSimple = compress(charsSimple)
    assert actualSimple == expectedSimple
    print(f"Yes! Compressed {charsSimple} to array of len {actualSimple}")

    charsComplex = ["a", "b", "b", "b", "c", "c"]
    # expectedComplex = ["a", 1, "b", 3, "c", 2]
    expectedComplex = 6
    actualComplex = compress(charsComplex)
    assert actualComplex == expectedComplex
    print(f"Yes! Compressed {charsComplex} to array of len {actualComplex}")