# Rappresentazione di un grafo orientato con pesi, usando una lista di liste di incidenza.

from typing import Iterator

class Graph:
    _data_edges: list[float]
    _data: list[tuple[set[int],set[int]]]

    def __init__(self, numnodes:int):
        self._data = [(set(), set()) for _ in range(numnodes)]
        self._edges = []
        
    def add_edge(self, n1: int, n2: int, weight: float) -> None:
        # Complex: O(1)
        i = len(self._edges)
        self._edges.append(weight)
        self._data[n1][0].add(i)
        self._data[n2][1].add(i)

    def get_edge(self, n1: int, n2: int) -> float | None:
        # Complex: O(?)
        common = self._data[n1][0] & self._data[n2][1]
        if common:
            return self._edges[common.pop()]
        return None

    def neighbors(self, node: int) -> Iterator[tuple[int, float]]:
        # Complex: O(?)
        for i in self._data[node][0]:
            n2 = next(n for n, (out, inc) in enumerate(self._data) if i in inc)
            yield (n2, self._edges[i])

   



