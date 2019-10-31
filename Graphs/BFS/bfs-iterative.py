# BFS (breadth-first search)
# Good for traversing nodes in trees and graphs only once
# Better than DFS for finding shortest path to a node from
# an arbitrary node (b/c you won't be travelling deep into
# one or more paths that may not take you to the node for 
# which you're looking)

# Iterative approach
# Time: O(n)  -> visit each node in tree w/ n nodes once
# Space: O(n) -> path list and queue each take up n space

# Note about recursive approach: since BFS uses a queue to
# determine which node to visit next, it'd be difficult to
# implement BFS recursively without a queue since recursion 
# relies on the stack data structure which operates in an 
# opposite manner to a queue. For example, DFS lends itself 
# naturally to how a stack operates and can therefore rely
# on a running computer program's call stack. (In DFS, we
# visit the last node that we've visited to process and then
# to determine the next node to visit, a "greedy" order which
# takes us deeper and deeper down a tree.)

from typing import List
from collections import deque

class Graph:
    def __init__(self, val):
        self.vertex_neighbours = {}

def bfs(start: int, graph: Graph):
    q, visited = deque([start]), []

    if not graph:
        return visited

    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        visited.append(curr)
        for neighbour in graph[curr]:
            q.append(neighbour)
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
    expected = [1, 2, 5, 6, 3, 4]
    actual = bfs(start, graph)
    assert actual == expected
    print(f"Woot, DFS on given graph gives: {actual}")

    graph = {}
    start = 0
    expected = []
    actual = bfs(start, graph)
    assert actual == expected
    print(f"Woot, DFS on given graph gives: {actual}")

    graph = { 0: [] }
    start = 0
    expected = [0]
    actual = bfs(start, graph)
    assert actual == expected
    print(f"Woot, DFS on given graph gives: {actual}")