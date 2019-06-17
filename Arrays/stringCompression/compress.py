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
    # currCharIdx = 0
    # currCharRunnerIdx = 0
    # charCount = 0
    # currIdx = 0
    # store a tuple with char and count in chrono order in chars
    runner = 0
    count = 0
    currCharIdx = 0
    while runner < len(chars)
        while chars[currCharIdx] == chars[runner]:
            count += 1
            runner += 1
        chars[currCharIdx] = (chars[currCharIdx], count)
        currCharIdx += 1
        count = 0
    numUniqueChars = currCharIdx + 1
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
    else:
        # normal case
        temp = chars[counter]
        moveByOne(chars, counter, numUniqueChars - counter)
        chars[counter], chars[counter + 1] = chars[counter][0], chars[counter][1]
    # while currCharRunnerIdx < len(chars):
    #     while chars[currCharRunnerIdx] == chars[currCharIdx]:
    #         charCount += 1
    #         currCharRunnerIdx += 1
        
    #     if charCount == 1:
    #         chars[currIdx] = chars[currCharIdx]
    #         charCount = 0
    #         currIdx += 1
    #     else:
    #         chars[currIdx] = chars[currCharIdx]
    #         chars[currIdx + 1] = charCount
    #         charCount = 0
    #         currIdx += 2
    #     currCharRunnerIdx += + 1
    # result = chars[:currIdx + 1]
    return len(result)

def moveByOne(chars: List[str], currIdx: int, lenOfRemList: int):
    count = 0
    while count < lenOfRemList:
        chars[count + 1] = chars[currIdx]

# def countOneChars(chars: List[str], numUniqueChars: int):
#     idx = 0
#     numOneChars = 0
#     while idx < numUniqueChars:
#         if chars[idx][1] == 1:
#             numOneChars += 1
#     return numOneChars

# def findNumUniqueChars(chars: List[str]):
#     count = 1
#     front, back = 0, 1
#     while back < len(chars):
#         if chars[front] != chars[back]:
#             count += 1
#         front += 1
#         back += 1
#     return count 

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