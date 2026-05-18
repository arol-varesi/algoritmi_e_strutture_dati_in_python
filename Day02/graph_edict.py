# Graph rappresentato tramite lista di edges rappresentati da dizionario
from typing import Iterator

class Graph:
    _data: dict[tuple[int, int], float]

    def __init__(self, numnodes:int = 0):
        self._data = {}
        
    def add_edge(self, n1: int, n2: int, weight: float) -> None:
        # Complex: O(1)
        self._data[(n1, n2)] = weight


    def get_edge(self, n1: int, n2: int) -> float | None:
        # Complex: O(1)
        return self._data.get((n1, n2))

    def neighbors(self, node: int) -> Iterator[tuple[int, float]]:
    # Complex: O(|E|)
        for (n1, n2), weight in self._data.items():
            if n1 == node:
                yield (n2, weight)



