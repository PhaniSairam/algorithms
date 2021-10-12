from heapq import heappop, heappush
from collections import defaultdict


class Graph:
    def __init__(self, edge, vertex):
        self.edge = set(frozenset([u, v, c]) for u, v, c in edge)
        self._neighbours = defaultdict(list)
        for ele in vertex:
            self.addVertex(ele)
        for u, v, c in edge:
            self.addEdge(u, v, c)

    def addEdge(self, u, v, cost):
        self.edge.add(frozenset([u, v, cost]))
        if not [v, cost] in self._neighbours[u]:
            self._neighbours[u].append([v, cost])
        if not [u, cost] in self._neighbours[v]:
            self._neighbours[v].append([u, cost])

    def addVertex(self, v):
        if v not in self._neighbours:
            self._neighbours.setdefault(v, [])

    def neighbours(self, vertex):
        return self._neighbours[vertex]

    def get_just_neighbours(self, vertex):
        return [i[0] for i in self._neighbours[vertex]]

    def shortest_path(self, src, dest):
        queue = []
        heappush(queue, (0, src, []))
        print(f"First Element - {(0, src, [])}")
        visited = set()
        while queue:
            cur_cost, cur_vertex, path = heappop(queue)
            if cur_vertex not in visited:
                visited.add(cur_vertex)
                path = path + [cur_vertex]
                if cur_vertex == dest:
                    print(
                        f"Path Exists {src} to {dest} with cost {cur_cost}, path - {path}"
                    )
                    # break
                for neighbour, neigh_cost in self.neighbours(cur_vertex):
                    print(f"Heap Element - {(cur_cost + neigh_cost, neighbour, path)}")
                    heappush(queue, (cur_cost + neigh_cost, neighbour, path))
        # print(f"shorted path - {queue[0]}")
        print(f"Complete Path - {queue}")

    @property
    def numOfEdges(self):
        return len(self.edge)

    @property
    def numOfVertex(self):
        return len(self._neighbours)


if __name__ == "__main__":
    vertex = {"Mumbai", "Paris", "Dubai", "New York", "Toronto", "Hawai"}
    routes = {
        ("Mumbai", "Paris", 7),
        ("Mumbai", "Dubai", 11),
        ("Hawai", "Toronto", 2),
        ("Paris", "Dubai", 3),
        ("Paris", "Hawai", 2),
        ("Hawai", "New York", 6),
        ("Dubai", "Toronto", 1),
        ("Toronto", "New York", 2),
    }
    graph = Graph(vertex=vertex, edge=routes)
    assert graph.numOfVertex == 6 and graph.numOfEdges == 8
    assert set(graph.get_just_neighbours("Hawai")) == {"Paris", "Toronto", "New York"}
    graph.shortest_path("Mumbai", "Dubai")
    print("Okay")
