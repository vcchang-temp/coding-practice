# Most common word
# (find most common word in a given paragraph that also
# doesn't appear on a banned list)

# Input: string paragraph, list banned

# Time: O(n + m)  -> check every word in paragraph with
#                    n words; each word with m punctuation
#                    symbols
# Space: O(n + m) -> space needed is proportional to n
#                    words and m punctuation symbols in 
#                    paragraph

from typing import List

def findMostCommonWord(paragraph: str, banned: List[str]):
    words = paragraph.split()
    punctuation = ['!', '?', "'", ',', ';', '.']
    
    trimmedWords = []     
    for word in words:
        trimmedWord = []
        if word[0] in punctuation or word[len(word)-1] in punctuation:
            trimmedWord.extend(trim(word.lower(), punctuation))
        else:
            trimmedWord.append(word.lower())
        trimmedWords.extend(trimmedWord)

    trimmedWordsDict = {}
    for trimmedWord in trimmedWords:
        if trimmedWord not in banned:
            if trimmedWord not in trimmedWordsDict:
                trimmedWordsDict[trimmedWord] = 1
            else:
                trimmedWordsDict[trimmedWord] += 1

    return max(trimmedWordsDict, key=trimmedWordsDict.get)
    
def trim(word: str, punctuation: List[str]):
    words = []    
    for punc in punctuation:
        splitWords = []
        splitWords = word.split(punc)
        if len(splitWords) > 1:
            words.extend(splitWords)

    trimmedWords = []
    for word in words:
        if word:
            trimmedWords.append(word)

    return trimmedWords

if __name__ == "__main__":
    paragraph = "Mom cooked me some delicious curry! I love me some curry. Yum, yum..."
    banned = ["curry", "yum"]
    expected = "me"
    actual = findMostCommonWord(paragraph, banned)
    assert actual == expected
    print(f"yass we got the most common word --> '{actual}' :)")