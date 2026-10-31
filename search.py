"""
AI Assignment: Uninformed (Blind) Search
Algorithms: BFS, DFS, DLS, IDDFS, UCS
Run: python search.py
"""
from collections import deque
import heapq

# Directed weighted graph: node -> [(neighbor, step_cost), ...]
GRAPH = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1), ('E', 3)],
    'C': [('G', 6)],
    'D': [('G', 2)],
    'E': [('G', 5)],
    'G': [],
}


def path_cost(path):
    """Total cost of a path of nodes."""
    cost = 0
    for u, v in zip(path, path[1:]):
        cost += dict(GRAPH[u])[v]
    return cost


def bfs(start, goal):
    frontier = deque([start])
    parent = {start: None}
    order = []
    while frontier:
        node = frontier.popleft()
        order.append(node)
        if node == goal:
            return build_path(parent, goal), order
        for nxt, _ in GRAPH[node]:
            if nxt not in parent:
                parent[nxt] = node
                frontier.append(nxt)
    return None, order


def dfs(start, goal):
    stack = [start]
    parent = {start: None}
    order = []
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        if node == goal:
            return build_path(parent, goal), order
        # reversed so the first neighbor is explored first
        for nxt, _ in reversed(GRAPH[node]):
            if nxt not in visited:
                parent[nxt] = node
                stack.append(nxt)
    return None, order


def dls(start, goal, limit):
    order = []

    def recurse(node, depth, path):
        order.append(node)
        if node == goal:
            return path
        if depth == limit:
            return None  # cutoff
        for nxt, _ in GRAPH[node]:
            if nxt not in path:  # avoid cycles on current path
                result = recurse(nxt, depth + 1, path + [nxt])
                if result:
                    return result
        return None

    return recurse(start, 0, [start]), order


def iddfs(start, goal, max_depth=10):
    total_order = []
    for limit in range(max_depth + 1):
        path, order = dls(start, goal, limit)
        total_order.append((limit, order))
        if path:
            return path, limit, total_order
    return None, None, total_order


def ucs(start, goal):
    frontier = [(0, start)]
    parent = {start: None}
    best = {start: 0}
    order = []
    explored = set()
    while frontier:
        cost, node = heapq.heappop(frontier)
        if node in explored:
            continue
        explored.add(node)
        order.append(node)
        if node == goal:
            return build_path(parent, goal), cost, order
        for nxt, w in GRAPH[node]:
            new_cost = cost + w
            if nxt not in best or new_cost < best[nxt]:
                best[nxt] = new_cost
                parent[nxt] = node
                heapq.heappush(frontier, (new_cost, nxt))
    return None, float('inf'), order


def build_path(parent, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]
    return path[::-1]


def show(name, path, order, extra=""):
    if path:
        print(f"{name:6} Path: {' -> '.join(path)} | Cost: {path_cost(path)} {extra}")
    else:
        print(f"{name:6} No path found {extra}")
    print(f"       Expansion order: {' '.join(order)}\n")


if __name__ == "__main__":
    START, GOAL = 'S', 'G'
    print(f"Start = {START}, Goal = {GOAL}\n")

    p, o = bfs(START, GOAL)
    show("BFS", p, o)

    p, o = dfs(START, GOAL)
    show("DFS", p, o)

    p, o = dls(START, GOAL, 2)
    show("DLS(2)", p, o, "(limit too small)")

    p, o = dls(START, GOAL, 3)
    show("DLS(3)", p, o)

    p, depth, runs = iddfs(START, GOAL)
    flat = [n for _, order in runs for n in order]
    show("IDDFS", p, flat, f"(found at depth {depth})")

    p, c, o = ucs(START, GOAL)
    show("UCS", p, o, "(optimal)")
