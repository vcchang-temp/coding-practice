# Reverse Only Letters

# Time: O(n)  -> visit at most half of chars in str of len n once
# Space: O(n) -> make list/str out of input of len n

def reverseOnlyLetters(S: str):
    s = list(S)
    start = 0
    end = len(s)-1
        
    while start < end:
        if isAscii(s[start]) and isAscii(s[end]):
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        else:
            if not isAscii(s[start]):
                start += 1
            if not isAscii(s[end]):
                end -= 1
    return "".join(s)
    
def isUpperCaseAsciiLetter(c: str):
    asciiDec = ord(c)
    return asciiDec >= 65 and asciiDec <= 90
    
def isLowerCaseAsciiLetter(c: str):
    asciiDec = ord(c)
    return asciiDec >= 97 and asciiDec <= 122
    
def isAscii(c: str):
    return isUpperCaseAsciiLetter(c) or isLowerCaseAsciiLetter(c)

if __name__ == "__main__":
    s = "ab-cd"
    expected = "dc-ba"
    actual = reverseOnlyLetters(s)
    assert actual == expected
    print(f"Reversed only letters in '{s}' to '{actual}'")

    s = "a-bC-dEf-ghIj"
    expected = "j-Ih-gfE-dCba"
    actual = reverseOnlyLetters(s)
    assert actual == expected
    print(f"Reversed only letters in '{s}' to '{actual}'")

    s = ""
    expected = ""
    actual = reverseOnlyLetters(s)
    assert actual == expected
    print(f"Reversed only letters in '{s}' to '{actual}'")