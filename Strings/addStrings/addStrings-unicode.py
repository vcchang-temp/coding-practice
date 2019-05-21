# Add strings

# Input: non-negative ints num1, num2, digits between 0-9

# Unicode approach
# Time: O(n)  -> iterate through each char once
# Space: O(n) -> need a list of len as long as number of digits
#                in num1 and a list of len as long as digits in
#                num2 

def addStrings(num1: str, num2: str):
    num1List = list(num1)
    num2List = list(num2)

    num1Dig, num2Dig, carry, resStr = 0, 0, 0, []
    while num1List or num2List:
        num1Dig = ord(num1List.pop()) - ord('0') if num1List else 0
        num2Dig = ord(num2List.pop()) - ord('0') if num2List else 0
        
        res = carry + num1Dig + num2Dig
        
        if res >= 10:
            carry = 1
            res = res % 10
        else:
            carry = 0

        resStr.insert(0, chr(res + ord('0')))
    
    return "".join(resStr)

if __name__ == "__main__":
    num1 = "1234"
    num2 = "291"
    expected = "1525"
    actual = addStrings(num1, num2)
    assert actual == expected
    print(f"Wohoo added strings correctly! {num1} + {num2} = {actual}")

    numOne = "1234"
    numTwo = "2918"
    expectedOneTwo = "4152"
    actualOneTwo = addStrings(numOne, numTwo)
    assert actualOneTwo == expectedOneTwo
    print(f"Yay added equally long strings correctly! {num1} + {num2} = {actualOneTwo}")

    first0 = "0"
    second0 = "0"
    expectedZero = "0"
    actualZero = addStrings(first0, second0)
    assert actualZero == expectedZero
    print(f"Added zero strings correctly! {first0} + {second0} = {actualZero}")