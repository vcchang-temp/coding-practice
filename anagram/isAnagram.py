# Anagram check

# Input: string s1, string s2

# Time: O(maxLen(n, m)) -> bounded by len of longest string
# Space: O(n + m) -> need space for dictionaries with n + m keys

def isAnagram(s1: str, s2: str):
    if s1 == None or s2 == None:
        return False
        
    s1Dict = makeDict(s1)
    s2Dict = makeDict(s2)
        
    return s1Dict == s2Dict
    
def makeDict(s: str) -> dict:
    dictionary = {}

    for i in range(len(s)):
        if s[i] in dictionary:
            dictionary[s[i]] += 1
        else:
            dictionary[s[i]] = 1

    return dictionary

if __name__ == "__main__":
    s1Anagram = "happea"
    s2Anagram = "peahap"
    anagramResult = isAnagram(s1Anagram, s2Anagram)
    assert anagramResult == True
    print(f"So {s1Anagram} that {s2Anagram} are anagrams!")

    s1NotAnagram = "hai"
    s2NotAnagram = "bai"
    notAnagramResult = isAnagram(s1NotAnagram, s2NotAnagram)
    assert notAnagramResult == False
    print(f"{s1NotAnagram} and {s2NotAnagram} are not anagrams...")