# Meeting Rooms I

# Given an array of meeting time intervals consisting 
# of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
# determine if a person could attend all meetings.

# For example, given [[0, 30],[5, 10],[15, 20]], return false.

# Time: O(nlogn) -> .sort takes O(nlogn) time
# Space: O(n)    -> create 2 arrays of len n each ~ O(n)

from typing import List

def canAttend(meetings: List[List[int]]) -> bool:
    meetings.sort(key=lambda m: m[0])
    startTimes = getStartTimes(meetings)
    endTimes = getEndTimes(meetings)

    i = 1
    for j in range(len(endTimes)-1):
        if endTimes[j] > startTimes[i]:
            return False
        i += 1
    return True

def getStartTimes(meetings: List[List[int]]) -> bool:
    times = []
    for m in meetings:
        times.append(m[0])
    return times

def getEndTimes(meetings: List[List[int]]) -> bool:
    times = []
    for m in meetings:
        times.append(m[1])
    return times

if __name__ == "__main__":
    meetings = [[5, 10],[15, 20],[0, 30]]
    actual = canAttend(meetings)
    assert actual == False
    print(f"Can attend meetings {meetings}? -> {actual}")

    meetings = [[5, 10],[15, 20]]
    actual = canAttend(meetings)
    assert actual == True
    print(f"Can attend meetings {meetings}? -> {actual}")

    meetings = [[15, 20], [5, 10]]
    actual = canAttend(meetings)
    assert actual == True
    print(f"Can attend meetings {meetings}? -> {actual}")