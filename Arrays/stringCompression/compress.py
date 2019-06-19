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
    runner = 0
    count = 0
    currCharIdx = 0
    nextCharIdx = 0
    while runner < len(chars):
        currChar = chars[nextCharIdx]
        while runner < len(chars) and chars[runner] == currChar:
            count += 1
            runner += 1
        chars[currCharIdx] = (currChar, count)
        currCharIdx += 1
        nextCharIdx += count
        count = 0
    numUniqueChars = currCharIdx + 1
    print(f"numUniqueChars: {numUniqueChars}")
    if numUniqueChars >= len(chars):
        return chars
    elif numUniqueChars * 2 > len(chars):
        # only expand the ones w/o a one char
        counter = 0
        while counter < numUniqueChars:
            if chars[counter][1] == 1:
                chars[counter] = chars[counter][0]
            else:
                temp = chars[counter]
                moveByOne(chars, counter, numUniqueChars - counter)
                chars[counter], chars[counter + 1] = chars[counter][0], chars[counter][1]
            counter += 1
    else:
        # normal case
        temp = chars[counter]
        moveByOne(chars, counter, numUniqueChars - counter)
        chars[counter], chars[counter + 1] = chars[counter][0], chars[counter][1]
    result = chars[numUniqueChars - counter]
    return len(result)

def moveByOne(chars: List[str], currIdx: int, lenOfRemList: int):
    count = 0
    while count < lenOfRemList:
        chars[count + 1] = chars[currIdx]

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
    
    # charsSimple = ["a", "b"]
    # # expectedSimple = ["a", "b"]
    # expectedSimple = 2
    # actualSimple = compress(charsSimple)
    # print(f"charsSimple: {charsSimple}")
    # assert actualSimple == expectedSimple
    # print(f"Yes! Compressed {charsSimple} to array of len {actualSimple}")

    charsComplex = ["a", "b", "b", "b", "c", "c"]
    # expectedComplex = ["a", 1, "b", 3, "c", 2]
    expectedComplex = 6
    actualComplex = compress(charsComplex)
    print(f"charsComplex: {charsComplex}")
    assert actualComplex == expectedComplex
    print(f"Yes! Compressed {charsComplex} to array of len {actualComplex}")