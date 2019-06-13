# Run-length decoding

# Input: (encoded) string s of len n

# Time: O(n)  -> iterate through each char in s
# Space: O(n*m) -> create new list/string with ~n/2
#                  chars times m total count (num)

def decode(s: str):
    if not s:
        return s
    decodedS = []
    i = 0
    while i < len(s)-1:
        j = i
        while s[j].isdigit():
            j += 1
        if j > i:
            num = int(s[i:j])
            while num > 0:
                decodedS.append(s[j])
                num -= 1
        i = j + 1
    return "".join(decodedS)

if __name__ == "__main__":
    sEmpty = ""
    expectedEmpty = ""
    actualEmpty = decode(sEmpty)
    assert actualEmpty == expectedEmpty
    print(f"Mission completed. Decoded '{sEmpty}' into '{actualEmpty}'.")

    sComplex = "4A3B2C11D2A"
    expectedComplex = "AAAABBBCCDDDDDDDDDDDAA"
    actualComplex = decode(sComplex)
    assert actualComplex == expectedComplex
    print(f"Mission completed. Encoded '{sComplex}' into '{actualComplex}'.")