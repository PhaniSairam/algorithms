from collections import defaultdict


class Graph:
    def __init__(self, vertex, edge):
        # self.vertex = set(vertex)
        # frozenset - we want vertices to be unordered sets, we cannot have sets of sets, so it is sets of frozem sets
        self.edge = set(frozenset((u, v)) for u, v in edge)
        # defaultdict is to map all the neighbours of each and every vertex/node
        self._neighbours = defaultdict(set)
        #  below vertex loop is needed if self._neighbours is a normal dict. for defaultdict,
        #  we dont need to add vertex and default to set
        #  if not exists, defaultdict, when creating edges, default dict will initialize vertex.
        # for v in vertex:
        #     self.addVertex(v)
        for u, v in self.edge:
            self.addEdge(u, v)
            # self._neighbours[u].add(v)
            # self._neighbours[v].add(u)

    # def addVertex(self, vertex):
    # self.vertex.add(vertex)
    # if vertex not in self._neighbours:
    # self._neighbours[vertex]= set()
    # self._neighbours.setdefault(vertex)

    def addEdge(self, u, v):
        # self.addVertex(u)
        # self.addVertex(v)
        self.edge.add(frozenset([u, v]))
        self._neighbours[u].add(v)
        self._neighbours[v].add(u)

    def degree(self, vertex):
        # return sum(1 for e in self.edge if vertex in e)
        return len(self._neighbours[vertex])

    def neighbours(self, vertex):
        return self._neighbours[vertex]

    def removeEdge(self, u, v):
        edge = frozenset([u, v])
        if edge in self.edge:
            # this condition is needed to prevent keyerror's i.e if non existing edges were passed to this function,
            # this should not throw error. So we remove only if edge exists, else do nothing as edge doesnt exist
            self.edge.remove(edge)
            self._neighbours[u].remove(v)
            self._neighbours[v].remove(u)

    def removeVertex(self, vertex):
        # to delete is needed, during iteration of self.neighbours,
        # I cannot delete, otherwise python will throw runtime error. Set changed size during iteration
        todelete = list(self.neighbours(vertex))
        for v in todelete:
            self.removeEdge(vertex, v)
        del self._neighbours[vertex]

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
    graph = Graph({1, 2, 3}, {(1, 2), (2, 3)})
    assert graph.degree(1) == 1
    assert graph.degree(2) == 2
    assert graph.degree(3) == 1
    assert set(graph.neighbours(2)) == {1, 3}
    assert set(graph.neighbours(1)) == {2}
    assert set(graph.neighbours(3)) == {2}
    assert graph.numOfVertex == 3 and graph.numOfEdges == 2
    graph.removeEdge(1, 2)
    assert graph.numOfVertex == 3 and graph.numOfEdges == 1
    graph.removeEdge(
        1, 3
    )  # this edge doesnt exist. the if condition in removeEdge prevents this program from failure with KeyError
    assert graph.numOfVertex == 3 and graph.numOfEdges == 1
    graph.addEdge(1, 2)
    assert graph.numOfVertex == 3 and graph.numOfEdges == 2
    graph.removeVertex(2)
    assert graph.numOfVertex == 2 and graph.numOfEdges == 0
    print("Okay")

    routes = {
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    }
    new_graph = Graph(
        {"Mumbai", "Paris", "Dubai", "New York", "Toronto"}, routes
    )
    print(new_graph.get_paths("Mumbai", "New York"))
