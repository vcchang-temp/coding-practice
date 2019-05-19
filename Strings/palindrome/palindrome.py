# Palindrome check

# Palindrome: string spelt the same forwards and backwards

# Input: non-empty string s

# Assumptions: no spaces in s

# Front and back pointer approach
# Time: O(n)  -> compare char of s of len n;
#                checking n/2 chars -> O(n/2) ~= O(n)
# Space: O(1) -> space needed does not grow with given input

def isPalindrome(s: str):
    front = 0
    back = len(s) - 1

    while front < back:
        if s[front] != s[back]:
            return False
        front += 1
        back  -= 1
    return True

if __name__ == "__main__":
    evenPalindrome = "anna"
    actualEven = isPalindrome(evenPalindrome)
    assert actualEven == True
    print("Yeayy, a palindrome with an even count of characters!")

    oddPalindrome = "racecar"
    actualOdd = isPalindrome(oddPalindrome)
    assert actualEven == True
    print("Wooo, a palindrome with an odd count of characters!")

    notAPalindrome = "anstna"
    actualNotP = isPalindrome(notAPalindrome)
    assert actualNotP == False
    print("Boo, not a palindrome :'(")