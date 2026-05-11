# Esercizio: Voti
# Genera una lista di 20 voti casuali compresi tra 18 e 30.
# Ordina la lista dei voti in modo crescente.
# Utilizza il modulo `bisect` per inserire un nuovo voto nella lista mantenendo l'ordine.
# Stampa la posizione in cui è stato inserito il nuovo voto e la lista aggiornata dei voti.


from random import randint, seed
import bisect
from icecream import ic


NUM_VOTI = 20

def main():
    seed(42)  # For reproducible results
    votes = [randint(18, 30) for _ in range(NUM_VOTI)]
    votes.sort()
    ic(votes)

    new_vote = randint(18, 30)
    left = bisect.bisect_left(votes, new_vote)
    right = bisect.bisect_right(votes, new_vote)

    bisect.insort(votes, new_vote)

    ic(new_vote, left, right)


if __name__ == "__main__":
    main()