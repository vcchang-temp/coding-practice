# Palindrome check

# Palindrome: string spelt the same forwards and backwards

# Input: non-empty string s

# Assumptions: no spaces in s

# Reverse string approach
# Time: O(n)  -> check each character in s of len n
# Space: O(n) -> new string needs n space

def isPalindrome(s: str):
    reversedS = ""

    for i in reversed(range(len(s))):
        reversedS += s[i]
    
    return s == reversedS

if __name__ == "__main__":
    evenPalindrome = "hannah"
    actualEven = isPalindrome(evenPalindrome)
    assert actualEven == True
    print("Yeayy, a palindrome with an even count of characters!")

    oddPalindrome = "radar"
    actualOdd = isPalindrome(oddPalindrome)
    assert actualEven == True
    print("Wooo, a palindrome with an odd count of characters!")

    notAPalindrome = "blah"
    actualNotP = isPalindrome(notAPalindrome)
    assert actualNotP == False
    print("Boo, not a palindrome :'(")