# Test per la classe Graph implementata in graph_dict.py

#FILENAME = 'data/ALL_hcp/alb1000.hcp'
#FILENAME = 'data/ALL_tsp/tsp225.tsp'
FILENAME = 'data/ALL_tsp/brd14051.tsp'

from random import seed, randint, random
from icecream import ic
from itertools import product
from read_graph import read_graph, Graph
from collections import deque
import heapq



def bfv(G: Graph, node: int) -> list[int]:
    """Breadth-First Visit: visita in ampiezza di un grafo, partendo da un nodo dato."""
    discovered = set()
    frontier = deque()
    discovered.add(node)
    frontier.append(node)
    visit = list()

    while frontier:
        node = frontier.popleft()
        visit.append(node)

        for n, _ in G.neighbors(node):
            if n not in discovered:
                discovered.add(n)
                frontier.append(n)
    return visit

def dfv(G: Graph, node: int) -> list[int]:
    discovered = set()
    frontier = deque()
    discovered.add(node)
    frontier.append(node)
    visit = list()

    while frontier:
        node = frontier.pop()
        visit.append(node)

        for n, _ in reversed(list(G.neighbors(node))):
            if n not in discovered:
                discovered.add(n)
                frontier.append(n)
    return visit

def shortest_path(G: Graph, n1: int, n2: int) -> list[int]:
    """Breadth-First Visit: visita in ampiezza di un grafo, partendo da un nodo dato."""
    
    path: dict[int, int | None] = {n1: None} # dizionario che memorizza il nodo precedente per ogni nodo visitato
    frontier = [(0.0, n1)]

    while frontier:
        cost, current = heapq.heappop(frontier)
        if current == n2:
            break
        for n, w in G.neighbors(current):
            if n not in path:
                path[n] = current
                heapq.heappush(frontier, (cost + w, n))
    else:
        return list()
    # Ricostruisce il percorso
    p = list()
    while current is not None:
        p.append(current)
        current = path[current]
    ic("Shortest path found")
    return p[::-1]


def main():

    G = read_graph(FILENAME)
    
    seed(42)
    for n1, n2 in product(range(len(G)), repeat=2):
        if random() < 0.9:
            G.del_edge(n1, n2)

    # visit = bfv(G, 0)
    # visit_dfs = dfv(G, 0)
    # print(f"0x{hash(tuple(visit)):X}")
    # print(f"0x{hash(tuple(visit_dfs)):X}")

    path = shortest_path(G, 42, 99)
    ic(path)
    tot = 0
    for n1, n2 in zip(path, path[1:]):
        tot += G.get_edge(n1, n2) or 0.0
        print(f"{n1} -> {n2} (weight: {G.get_edge(n1, n2)})")
    print(f"Total weight: {tot}")

if __name__ == "__main__":
    main()