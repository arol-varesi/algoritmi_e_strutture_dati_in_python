# Esercizio 1
# Un pronto soccorso riceve pazienti con diversi livelli di priorità.
# Ogni paziente ha un nome e una priorità (un numero intero, dove 0 è la massima priorità).
# Il pronto soccorso deve gestire i pazienti in modo che quelli con priorità più alta vengano trattati prima.
# Se due pazienti hanno la stessa priorità, devono essere trattati in ordine di arrivo.
# Implementa una classe `Patient` che rappresenta un paziente, con attributi per il nome,
# la priorità e un timestamp per l'ordine di arrivo. 
# Utilizza una coda di priorità per gestire i pazienti in modo efficiente.

from dataclasses import dataclass, field
import time
import heapq        # per la gestione della coda di priorità

@dataclass(order=True)
class Patient:
    priority: int
    timestamp: float
    name: str = field(compare=False)

    def __init__( self, name: str, priority: int) -> None:
        self.name = name
        self.priority = priority
        self.timestamp = time.time()

def main():
    pazienti = list()

    pazienti.append(Patient("Mario Rossi", 2))
    pazienti.append(Patient("Luigi Bianchi", 1))
    pazienti.append(Patient("Giovanni Verdi", 2))
    pazienti.append(Patient("Anna Neri", 3))
    pazienti.append(Patient("Sara Gialli", 1))
    pazienti.append(Patient("Paolo Blu", 2))
    pazienti.append(Patient("Laura Viola", 3))

    print(pazienti)

    # Creazione della coda di priorità
    heapq.heapify(pazienti)

    # Inserimento del nuovo paziente nella coda di priorità
    heapq.heappush(pazienti, Patient("Francesco Arancio", 0))

    # Estrazione dei pazienti in ordine di priorità
    print("Ordine di estrazione dei pazienti:")
    while pazienti:
        paziente = heapq.heappop(pazienti)
        print(f"{paziente.name} (priorità: {paziente.priority})") 
        

if __name__ == "__main__":
    main()