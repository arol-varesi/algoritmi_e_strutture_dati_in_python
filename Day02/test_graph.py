# Test per la classe Graph implementata in graph_dict.py

from icecream import ic
from graph_edge_inc import Graph

def main():
    G = Graph(5)
    G.add_edge(1, 3, 1.0)
    G.add_edge(3, 1, 1.0)
    G.add_edge(2, 3, 2.0)
    G.add_edge(3, 2, 2.0)

    ic (G._data)

    ic (G.get_edge(1, 3))

    ic (list(G.neighbors(3)))


    # graph.add_edge('A', 'B')
    # graph.add_edge('A', 'C')
    # graph.add_edge('B', 'D')
    # graph.add_edge('C', 'D')
    # graph.add_edge('D', 'E')

    #ic(graph.adjacency_list)

if __name__ == "__main__":
    main()