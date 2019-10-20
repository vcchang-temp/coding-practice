# Minimum window substring

# Time: O(s + t)  -> s = length of search string, t = length of target string
#                    s = need to traverse string at most twice
#                    t = time taken to build dictionary with target chars
# Space: O(s + t) -> answer may at most be of len s and dictionary takes up len t space

from collections import Counter

def minWindow(s: str, t: str):
    if not s or not t:
        return ""
    
    targetChars = Counter(t)
    targetUniqueCharsCount = len(targetChars)

    left, right = 0, 0

    currWindowTargetSatisfactionLevel = 0
    currWindow = dict()

    currOptimalWindow = float("inf"), None, None

    while right < len(s):
        currChar = s[right]
        currWindow[currChar] = currWindow.get(currChar, 0) + 1 # return 0 if currChar has not been seen

        if currChar in targetChars and currWindow[currChar] == targetChars[currChar]:
            currWindowTargetSatisfactionLevel += 1
        
        # enter inner loop when want to contract to try and find smaller window
        while left <= right and currWindowTargetSatisfactionLevel == targetUniqueCharsCount:
            currChar = s[left]

            # save smallest window so far
            if (right - left + 1) < currOptimalWindow[0]:
                currOptimalWindow = (right - left + 1, left, right)
            
            # take one occurrence of left char out of curr window
            currWindow[currChar] -= 1
            if currChar in targetChars and currWindow[currChar] < targetChars[currChar]:
                currWindowTargetSatisfactionLevel -= 1
            
            left += 1

        # outer loop keeps expanding until current window satisfies
        right += 1
    
    return "" if currOptimalWindow[0] == float("inf") else s[currOptimalWindow[1] : currOptimalWindow[2] + 1]

if __name__ == "__main__":
    s = "ABBABEST"
    t = "AT"
    expected = "ABEST"
    actual = minWindow(s, t)
    assert actual == expected
    print(f"Yay, found the minimum substring of {s} given {t}: {actual}")

    s = "howonearthdoyoufindthisstring"
    t = "eyo"
    expected = "earthdoy"
    actual = minWindow(s, t)
    assert actual == expected
    print(f"Yay, found the minimum substring of {s} given {t}: {actual}")

    s = "what"
    t = ""
    expected = ""
    actual = minWindow(s, t)
    assert actual == expected
    print(f"Yay, found the minimum substring of {s} given {t}: {actual}")

    s = ""
    t = "why"
    expected = ""
    actual = minWindow(s, t)
    assert actual == expected
    print(f"Yay, found the minimum substring of {s} given {t}: {actual}")