# DFS (depth-first search)
# Good for traversing nodes in trees and graphs only once

# Recursive approach
# Time: O(n)  -> visit each node in graph w/ n nodes once
# Space: O(n) -> visited list takes up n space.
#                call stack can also take up - in worst case -
#                n space (graph that's a straight line)

from typing import List

class Graph:
    def __init__(self, val):
        self.vertex_neighbours = {}

def dfs(start: int, graph: Graph):
    visited = []

    if not graph:
        return visited

    return dfsHelper(start, graph, visited)

def dfsHelper(vertex: int, graph: Graph, visited: List):
    if vertex not in visited:
        visited.append(vertex)
        for neighbour in graph[vertex]:
            dfsHelper(neighbour, graph, visited)
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
    expected = [1, 2, 3, 5, 4, 6]
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