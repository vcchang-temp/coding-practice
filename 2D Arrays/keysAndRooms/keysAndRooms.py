# Keys and Rooms

# Time: O(n)  -> in worst case, all rooms contain keys 
#                to all but one room, so n-1 rooms x 
#                n-1 keys ~= n^2 (n = number of rooms)
# Space: O(n) -> create stack and visited array that each
#                may reach n height (due to stack potentially
#                collecting all possible keys) and array is
#                initialized to n elements

from typing import List

def canVisitAllRooms(rooms: List[List[int]]):
    stack = rooms[0]
    visited = [False] * len(rooms)
    visited[0] = True
    while stack:
        key = stack.pop()
        if not visited[key]:
            stack.extend(rooms[key])
            visited[key] = True
    return False if False in visited else True

if __name__ == "__main__":
    rooms = [[1],[2],[3],[]]
    actual = canVisitAllRooms(rooms)
    assert actual == True
    print(f"Yay can visit all rooms in {actual}!")

    rooms = [[1,3],[3,0,1],[2],[0]]
    actual = canVisitAllRooms(rooms)
    assert actual == False
    print(f"Yay can visit all rooms in {actual}!")