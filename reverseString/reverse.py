# Reverse a string

# Time: O(n) -> must go through each letter in string of n length
# Space: O(n) -> create new string of length n

def reverse(s: str):
    if s == None:
        return ""
    reversedStr = ""

    for i in reversed(range(len(s))):
        reversedStr += s[i]
    
    return reversedStr

if __name__ == "__main__":
    expected = "gnirts"
    actual = reverse("string")
    assert actual == expected
    print("Yes, string reversed!")