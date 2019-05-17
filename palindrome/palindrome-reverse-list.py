# Palindrome check

# Palindrome: string spelt the same forwards and backwards

# Input: non-empty string s

# Assumptions: no spaces in s

# Reverse list approach
# Time: O(n)  -> push each char in s onto list
#                (no need to create new list each time append
#                 new char, unlike when creating new string
#                 and needing to copy each char to new string)
# Space: O(n) -> new string needs n space


def isPalindrome(s: str):
    reversedList = []

    for i in reversed(range(len(s))):
        reversedList.append(s[i])
    
    return s == "".join(reversedList)

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