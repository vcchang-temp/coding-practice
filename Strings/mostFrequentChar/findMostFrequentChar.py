# Most frequent character
# (find most frequent character; if there's a tie,
# return all chars in the tie)

# Input: string s

# Time: O(n)  -> iterate through each char to put into dict
# Space: O(n) -> dict will have as many k, v pairs as n chars of s

def findMostFreqChar(s: str):
    if s == None:
        return ""

    charFreqs = {}
    for i in range(len(s)):
        if s[i] not in charFreqs:
            charFreqs[s[i]] = 1
        else:
            charFreqs[s[i]] += 1

    maxFreq = max(charFreqs.values())
    result = [char for char, freq in charFreqs.items() if freq == maxFreq] # list comprehension

    return result

if __name__ == "__main__":
    oneMostFreqChar = "sshhhhsh"
    expectedOne = ["h"]
    actualOne = findMostFreqChar(oneMostFreqChar)
    assert expectedOne == actualOne
    print(f"Woot, found most frequent character in {oneMostFreqChar} which is {actualOne}")

    manyMostFreqChar = "yahyah"
    expectedMany = ["y", "a", "h"]
    actualMany = findMostFreqChar(manyMostFreqChar)
    assert expectedMany == actualMany
    print(f"Woot, found most frequent character in {manyMostFreqChar} which is {actualMany}")