class Graph:
    def __init__(self, vertex, edge):
        self.edge = set(frozenset((u, v)) for u, v in edge)
        self._neighbours = {}
        for v in vertex:
            self.addVertex(v)
        for u, v in edge:
            self.addEdge(u, v)

    def addVertex(self, v):
        if v not in self._neighbours:
            self._neighbours[v] = set()

    def addEdge(self, u, v):
        self.edge.add(frozenset([u, v]))
        if u not in self._neighbours:
            self.addVertex(u)
        if v not in self._neighbours:
            self.addVertex(v)
        self._neighbours[u].add(v)

    def neighbours(self, vertex):
        return self._neighbours[vertex]

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        paths = []
        if start == end:
            return [path]
        if start not in self._neighbours:
            return []
        for vertex in self._neighbours[start]:
            if vertex not in path:
                new_paths = self.get_paths(vertex, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    @property
    def numOfEdges(self):
        return len(self.edge)

    @property
    def numOfVertex(self):
        return len(self._neighbours)


if __name__ == "__main__":
    routes = {
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Hawai", "Toronto"),
        ("Paris", "Dubai"),
        ("Paris", "Hawai"),
        ("Hawai", "New York"),
        ("Dubai", "Toronto"),
        ("Toronto", "New York"),
    }
    graph = Graph({"Mumbai", "Paris", "Dubai", "New York", "Toronto"}, routes)
    print(graph.neighbours("Mumbai"))
    print(graph.get_paths("Mumbai", "New York"))
