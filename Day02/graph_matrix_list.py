# Rappresentazione di un grafo orientato con pesi, usando una matrice (lista di liste) di adiacenza.

class Graph:
    _data: list[list[float | None]]

    def __init__(self, numnodes:int):
        self._data = [[None] * numnodes for _ in range(numnodes)] 
        
    def add_edge(self, n1: int, n2: int, weight: float) -> None:
        # Complex: O(1)
        self._data[n1][n2] = weight

    def get_edge(self, n1: int, n2: int) -> float | None:
        # Complex: O(1)
        return self._data[n1][n2]
        ...

    def neighbors(self, node: int) -> Iterator[tuple[int, float]]:
        # Complex: O(|V|)
        #for i, weight in enumerate(self._data[node]):
        #    if weight is not None:
        #        yield (i, weight)

        return ((i, weight) for i, weight in enumerate(self._data[node]) if weight is not None )



