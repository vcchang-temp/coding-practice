# DFS (depth-first search)
# Good for traversing nodes in trees and graphs only once

# Iterative approach
# Time: O(n)  -> visit each node in graph w/ n nodes once
# Space: O(n) -> visited list takes up n space.
#                stack can also take up - in worst case -
#                n space (graph that's a straight line)

class Graph:
    def __init__(self, val):
        self.vertex_neighbours = {}

def dfs(start: int, graph: Graph):
    # could use set for visited, O(1) instead of O(n) lookup then
    stack, visited = [start], []

    if not graph:
        return visited

    while stack: # note how our fcn pushes elements onto the stack 
        vertex = stack.pop() # and pops the most recent vertex, 
        if vertex in visited: # resulting in a "reverse" order
            continue     
        visited.append(vertex)
        for neighbour in graph[vertex]:
            stack.append(neighbour)

    return visited

if __name__ == "__main__":
    graph = {
        1: [2, 5, 6],
        2: [3, 4],
        3: [5],
        4: [],
        5: [],
        6: []
    }
    start = 1
    expected = [1, 6, 5, 2, 4, 3]
    actual = dfs(start, graph)
    assert actual == expected
    print(f"Woot, DFS on given graph gives: {actual}")

    graph = {}
    start = 0
    expected = []
    actual = dfs(start, graph)
    assert actual == expected
    print(f"Woot, DFS on given graph gives: {actual}")

    graph = { 0: [] }
    start = 0
    expected = [0]
    actual = dfs(start, graph)
    assert actual == expected
    print(f"Woot, DFS on given graph gives: {actual}")