import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from heap import MinHeap


class Package:
    def __init__(self, pid, pri, dest, kg):
        self.package_id = pid
        self.priority = int(pri)
        self.destination = dest
        self.weight_kg = float(kg)


class Graph:
    def __init__(self):
        self.adj = {}
        self.nodes = []
        self.edges = []

    def add_node(self, n):
        if n not in self.adj:
            self.adj[n] = []
            self.nodes.append(n)

    def add_edge(self, u, v, w):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, w))
        self.edges.append((u, v, w))

    def summary(self):
        print("Nodes:", len(self.nodes))
        print("Edges:", len(self.edges))
        print("List:", ", ".join(sorted(self.nodes)))

    def dijkstra(self, start, end):
        dist = {n: float('inf') for n in self.nodes}
        prev = {n: None for n in self.nodes}
        dist[start] = 0
        seen = set()
        heap = MinHeap()
        heap.push(0, start)

        while not heap.empty():
            d, u = heap.pop()
            if u in seen:
                continue
            seen.add(u)
            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    heap.push(dist[v], v)

        if dist[end] == float('inf'):
            return None, []

        path = []
        cur = end
        while cur:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        return dist[end], path

    def has_cycle(self):
        white, gray, black = 0, 1, 2
        color = {n: white for n in self.nodes}
        cycle = []

        def dfs(u, path):
            color[u] = gray
            path.append(u)
            for v, _ in self.adj[u]:
                if color[v] == gray:
                    cycle.extend(path[path.index(v):])
                    return True
                if color[v] == white and dfs(v, path):
                    return True
            path.pop()
            color[u] = black
            return False

        for n in self.nodes:
            if color[n] == white:
                if dfs(n, []):
                    return True, list(set(cycle))
        return False, []

    def bellman_ford(self, start):
        dist = {n: float('inf') for n in self.nodes}
        dist[start] = 0
        for _ in range(len(self.nodes) - 1):
            for u, v, w in self.edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        neg = any(dist[u] + w < dist[v] for u, v, w in self.edges)
        return dist, neg