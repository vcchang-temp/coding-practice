# Given an array of N numbers from 1 to N. A number is confusing 
# if it becomes *another* number *in the array* after we rotate each 
# number in the digit by 180 degrees. 

# Only 0, 1, 6, 8, 9 are still valid numbers after rotation by 
# 180 degrees. Other digits are not valid after the rotation.

# Find the total number of the confusing numbers in this array.

# Follow-up: How do you find the total number of confusing numbers 
# in the array efficiently if N is big?

# Time: O(n)  -> go through each digit from 1 to n
# Space: O(n) -> create new strings of n digits ~ n 

from typing import List

def countConfusingNums(digits: List[int]) -> int:
    count = 0
    for d in digits:
        if isValidNum(d, len(digits)):
            count += 1
    return count

def isValidNum(digit: int, upperBound: int) -> int:
    validNums = {
        "0" : "0",
        "1" : "1",
        "6" : "9",
        "8" : "8",
        "9" : "6"
    }

    dStr = str(digit)
    confusingNum = []
    for n in dStr:
        if n in validNums:
            confusingNum.append(validNums[n])
        else:
            return False

    confusingNum = int("".join(confusingNum))
    return confusingNum != digit and confusingNum >= 1 and confusingNum <= upperBound

if __name__ == "__main__":
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    expected = 4 # [6, 9, 16, 19]
    actual = countConfusingNums(digits)
    assert actual == expected
    print(f"There are {actual} confusing numbers in {digits}")