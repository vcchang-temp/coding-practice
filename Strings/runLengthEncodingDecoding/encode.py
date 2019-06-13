# Run-length encoding

# Input: (decoded) string s of len n

# Time: O(n)  -> iterate through each char in s
# Space: O(n) -> create new string of len n

def encode(s: str):
    if not s:
        return s
    i = 0
    encodedS = []
    while i < len(s):
        currChar = s[i]
        j = i
        charCount = 0
        while j < len(s) and currChar == s[j]:
            charCount += 1
            j += 1
        encodedS.append(str(charCount))
        encodedS.append(currChar)
        i = j
    return "".join(encodedS)

if __name__ == "__main__":
    sEmpty = ""
    expectedEmpty = ""
    actualEmpty = encode(sEmpty)
    assert actualEmpty == expectedEmpty
    print(f"Mission completed. Encoded '{sEmpty}' into '{actualEmpty}'.")

    sComplex = "AAAABBBCCDAA"
    expectedComplex = "4A3B2C1D2A"
    actualComplex = encode(sComplex)
    assert actualComplex == expectedComplex
    print(f"Mission completed. Encoded '{sComplex}' into '{actualComplex}'.")