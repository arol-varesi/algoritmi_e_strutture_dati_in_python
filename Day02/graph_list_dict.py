# Rappresentazione di un grafo tramite lista di adiacenza memorizzata in un dizionario.


from typing import Iterator

class Graph:
    _data: list[dict[int, float]]

    def __init__(self, numnodes:int):
        self._data = [{} for _ in range(numnodes)]
        
    def add_edge(self, n1: int, n2: int, weight: float) -> None:
        # Complex: O(1)
        self._data[n1][n2] = weight


    def get_edge(self, n1: int, n2: int) -> float | None:
        # Complex: O(1)
        return self._data[n1].get(n2)
    

    def neighbors(self, node: int) -> Iterator[tuple[int, float]]:
        # Complex: O(1)
        return iter(self._data[node].items())



