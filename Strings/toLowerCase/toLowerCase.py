# To lower case

# Input: string s

# Time: O(n)  -> convert each char in s
# Space: O(n) -> create new list (and string) of length of s (n)

def toLowerCase(s: str):
    if s is None:
        return ""
        
    lowerCaseS = []
    for i in range(len(s)):
        unicodeCharDecimal = ord(s[i])
        unicodeUpperCaseA = 65
        unicodeUpperCaseZ = 90

        if unicodeCharDecimal >= unicodeUpperCaseA and unicodeCharDecimal <= unicodeUpperCaseZ:
            upperAndLowerCaseDiff = 32
            unicodeCharDecimal += upperAndLowerCaseDiff
            lowerCaseChar = chr(unicodeCharDecimal)
            lowerCaseS.append(lowerCaseChar)
        else:
            lowerCaseS.append(s[i])

    return "".join(lowerCaseS)

if __name__ == "__main__":
    testS = "LOWER CASE :)"
    expected = "lower case :)"
    actual = toLowerCase(testS)
    assert actual == expected
    print(f"Hooray, converted {testS} to {expected}.")