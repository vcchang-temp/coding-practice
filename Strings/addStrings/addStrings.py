# Add strings

# Input: non-negative ints num1, num2 between 0-9

# Math modulo and power approach
# Time: O(n^2)    -> convert 2n chars to digits and sum to string  
# Space: O(n + m) -> space to store n digits of each num
#                    and m key-value pairs for num dictionary

def addStrings(num1: str, num2: str):
    num1Number = convertToNum(num1)
    num2Number = convertToNum(num2)
        
    sumNumber = num1Number + num2Number
        
    return convertToStr(sumNumber)
        
def convertToNum(num: str):
    numDict = { "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9 }
    power, number = 0, 0
    for i in reversed(range(len(num))):
        digit = numDict[num[i]]
        number += digit * 10**power
        power += 1
    return number
    
def convertToStr(num: int):
    strDict = { 0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9" }
    string, power = [], 1
    if num == 0:
        string.append(strDict[num])
    while num > 0:
        modDivisor = 10**power
        remainder = num % modDivisor
        num -= remainder
        if remainder > 9:
            remainder /= 10**(power-1)
        power += 1
        string.insert(0, strDict[remainder])
    return "".join(string)

if __name__ == "__main__":
    num1 = "123"
    num2 = "291"
    expected = "414"
    actual = addStrings(num1, num2)
    assert actual == expected
    print("Added strings successfully!")