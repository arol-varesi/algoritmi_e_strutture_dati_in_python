# Rappresentazione di un grafo tramite lista di adiacenza memorizzata in una lista.

from typing import Iterator

class Graph:
    _data: list[list[tuple[int, float]]]

    def __init__(self, numnodes:int):
        self._data = [[] for _ in range(numnodes)]
        
    def add_edge(self, n1: int, n2: int, weight: float) -> None:
        # Complex: O(1)
        self._data[n1].append((n2, weight))


    def get_edge(self, n1: int, n2: int) -> float | None:
        # Complex: O(|E|) where |E| is the number of edges in the graph
        retvalue = [weight for neighbor, weight in self._data[n1] if neighbor == n2]
        #for neighbor, weight in self._data[n1]:
        #    if neighbor == n2:
        #        return weight
        return retvalue[0] if retvalue else None
    

    def neighbors(self, node: int) -> Iterator[tuple[int, float]]:
        # Complex: O(|E|) where |E| is the number of edges in the graph
        return iter(self._data[node])



