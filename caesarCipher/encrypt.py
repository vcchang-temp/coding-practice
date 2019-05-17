# Caesar cipher encryptor

# Encrypt a given string by shifting the letters by k
# positions in the alphabet

# Input: non-empty string, non-negative integer

# Assumptions: no capital letters or spaces

# Time: O(n)  -> transform each char in given string s of len n
# Space: O(n) -> returned string grows proportionally with given string length

def encrypt(s: str, k: int):
    encryptedS = ""
    begOfAlpha = 96
    endOfAlpha = 122

    for char in s:
        charDec = ord(char)
        shiftedCharDec = charDec + k
        
        while shiftedCharDec > endOfAlpha:
            shiftedCharDec = begOfAlpha + (shiftedCharDec % endOfAlpha)
        
        encryptedS += chr(shiftedCharDec)

    return encryptedS

if __name__ == "__main__":
    secret = "themoneyisinthemattress"
    expected = "ymjrtsjdnxnsymjrfyywjxx"
    actual = encrypt(secret, 5)
    assert actual == expected
    
    print("The secret is safe")