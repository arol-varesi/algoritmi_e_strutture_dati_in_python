# Blueprint per la classe Graph, da implementare in vari diversi modi.
from typing import Iterator

class Graph:
    _data: None

    def __init__(self, numnodes:int):
       ... 
        
    def add_edge(self, n1: int, n2: int, weight: float) -> None:
        # Complex: O(?)
        ...


    def get_edge(self, n1: int, n2: int) -> float | None:
        # Complex: O(?)
        ...

    def neighbors(self, node: int) -> Iterator[tuple[int, float]]:
        # Complex: O(?)
        ...



