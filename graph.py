"""
Depth-First Search (DFS): DFS is a search algorithm
that explores as far as possible along each branch before backtracking.
"""
from queue import PriorityQueue
from collections import deque

def dfs(graph, start):
    print("-----dfs-----")
    visited, stack = set(), [(start, [start])]
    while stack:
        node, path = stack.pop()
        if node not in visited:
            visited.add(node)
            print(f'States expanded to: {visited}, Path returned: {path}')
            if node == 'Goal':
                return path
            stack.extend((n, path + [n])
                         for n in graph[node] if n not in visited)
    return []


"""
Breadth-First Search (BFS): BFS is a search algorithm
that explores all the vertices of a graph in breadth-first order.
"""


def bfs(graph, start):
    print("-----bfs-----")
    visited, queue = set(), deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(f'States expanded to: {visited}, Path returned: {path}')
            if node == 'Goal':
                return path
            queue.extend((n, path + [n])
                         for n in graph[node] if n not in visited)
    return []


"""
Uniform Cost Search (UCS): UCS is a search algorithm
that expands the node with the lowest path cost.
"""


def ucs(graph, start, goal):
    print("-----ucs-----")
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start, [start]))

    while not queue.empty():
        cost, node, path = queue.get()
        if node not in visited:
            visited.add(node)
            print(f'States expanded to: {visited}, Path returned: {path}')
            if node == goal:
                return path
            for i in graph[node]:
                if i not in visited:
                    total_cost = cost + graph[node][i]
                    queue.put((total_cost, i, path + [i]))
    return []


"""
Greedy Search: Greedy search is a search algorithm 
that expands the node that is closest to the goal, as estimated by a heuristic.
"""


def greedy_search(graph, start, goal, heuristic):
    print("-----greedy_search-----")
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start, [start]))

    while not queue.empty():
        _, node, path = queue.get()
        if node not in visited:
            visited.add(node)
            print(f'States expanded to: {visited}, Path returned: {path}')
            if node == goal:
                return path
            for i in graph[node]:
                if i not in visited:
                    priority = heuristic[i]
                    queue.put((priority, i, path + [i]))
    return []


"""
A Search*: A* Search is a search algorithm that expands the node with the lowest value of g(n) + h(n), 
where g(n) is the actual cost from the start node and h(n) is the heuristic estimate to the goal.
"""


def a_star_search(graph, start, goal, heuristic):
    print("-----a_star_search-----")
    visited = set()
    queue = PriorityQueue()
    queue.put((0, 0, start, [start]))

    while not queue.empty():
        f, g, node, path = queue.get()
        if node not in visited:
            visited.add(node)
            print(f'States expanded to: {visited}, Path returned: {path}')
            if node == goal:
                return path
            for i in graph[node]:
                if i not in visited:
                    g_new = g + graph[node][i]
                    h = heuristic[i]
                    f_new = g_new + h
                    queue.put((f_new, g_new, i, path + [i]))

    return []


# Graph represented as a dictionary
graph = {
    'start': {'A': 2, 'B': 5, 'D': 5},
    'A': {'C': 4},
    'C': {'D': 1, 'Goal': 2},
    'D': {'Goal': 5},
    'B': {},
    'Goal': {}
}

# Heuristic represented as a dictionary
heuristic = {
    'start': 0,
    'A': 2,
    'B': 5,
    'C': 2,
    'D': 1,
    'Goal': 0
}


print(dfs(graph, 'start'))
print(bfs(graph, 'start'))
print(ucs(graph, 'start', 'Goal'))
print(greedy_search(graph, 'start', 'Goal', heuristic))
print(a_star_search(graph, 'start', 'Goal', heuristic))
