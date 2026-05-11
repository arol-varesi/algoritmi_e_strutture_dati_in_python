# Esercizio: Heap
# Genera una lista di 50 numeri casuali compresi tra 1 e 1000.
# Utilizza il modulo `heapq` per trasformare la lista in un heap.
# Estrai i primi 10 elementi dal heap e stampali in ordine crescente. 

from random import randint
import heapq


def main():
    heap = [randint(1, 1000) for _ in range(50)]
    heapq.heapify(heap)

    for _ in range(10):
        n = heapq.heappop(heap)
        print(n, end=" ")
    print()


if __name__ == "__main__":
    main()