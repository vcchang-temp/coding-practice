# Reverse Words in a String III

# Time: O(n)  -> .split takes O(n) time for s of len n;
#                reversing each word in total takes ~O(n) time
# Space: O(n) -> make list/string of len n

import math

def reverseWords(s: str):
    if not s:
        return s
    
    words = s.split(" ")
    res = []
    for word in words:
        w = reverse(word)
        res.append(w)
    return " ".join(res)

def reverse(word: str):
    w = list(word)
    start = 0
    end = len(w)-1
    mid = math.floor(len(w)/2)

    while start < mid:
        w[start], w[end] = w[end], w[start]
        start += 1
        end -= 1
    
    return "".join(w)

if __name__ == "__main__":
    s = "So let us melt, and make no noise,"
    expected = "oS tel su ,tlem dna ekam on ,esion"
    actual = reverseWords(s)
    assert actual == expected
    print(f"Reversed words in '{s}' -> '{actual}'")

    s = ""
    expected = ""
    actual = reverseWords(s)
    assert actual == expected
    print(f"Reversed words in '{s}' -> '{actual}'")

    s = "ba"
    expected = "ab"
    actual = reverseWords(s)
    assert actual == expected
    print(f"Reversed words in '{s}' -> '{actual}'")