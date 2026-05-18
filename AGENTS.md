# AGENTS.md — Algoritmi e Strutture Dati in Python

## Cos'è

Repository didattico per il workshop "Algorithms and Data Structures in Python (3 DAYS)". Non è una libreria o applicazione — è un insieme di esercizi svolti in aula, organizzati per giornate.

## Stack

- Python 3.14 (`.python-version`), richiede >=3.12
- Gestione pacchetti: `uv` (lockfile: `uv.lock`)
- Unica dipendenza runtime: `icecream` (debug printing)
- **Niente** test framework, linter, formatter, type checker, CI, o task runner

## Comandi

```bash
uv run python main.py                          # entrypoint placeholder
uv run python Day01/er.py                      # eseguire un esercizio
uv run python Day02/test_graph.py              # test manuale dei grafi
uv sync                                        # installa dipendenze
```

## Struttura

| Percorso | Contenuto |
|---|---|
| `main.py` | Placeholder (`print("Hello from ...")`) |
| `Day01/` | Heap, radix, er (coda priorità pazienti), voti, espressioni matematiche |
| `Day02/` | 5 implementazioni di grafi (list_list, list_dict, matrix_list, edict, edge_inc) + parser TSPLIB |
| `data/ALL_tsp/` | 143 file `.tsp` / `.opt.tour` in formato TSPLIB |
| `data/ALL_hcp/` | 10 file `.hcp` + optimal tour + generatore C (`tspleap.c`) |
| `data/ALL_hcp/tspleap.c` | Generatore di leaper graph per TSPLIB (compilabile con `cc`) |

## Convenzioni

- Nomi di variabili, commenti e README in **italiano**
- `if __name__ == "__main__": main()` in tutti gli script eseguibili
- I grafi usano nodi interi (0..n-1) e pesi `float`
- Il pacchetto `icecream` (`ic()`) è usato per debug output nei test

## Implementazioni grafo (Day02)

| File | Struttura interna | `get_edge` | `neighbors` |
|---|---|---|---|
| `graph_list_list.py` | `list[list[tuple[int, float]]]` | O(E) | iter |
| `graph_list_dict.py` | `list[dict[int, float]]` | O(1) | iter |
| `graph_matrix_list.py` | `list[list[float\|None]]` | O(1) | O(V) |
| `graph_edict.py` | `dict[tuple[int,int], float]` | O(1) | O(E) |
| `graph_edge_inc.py` | `list[tuple[set[int],set[int]]]` + `list[float]` | set intersection | O(E·V) |

## Noto: import rotto

`Day02/read_graph.py:7` importa `from graph_alist import Graph` ma `graph_alist.py` non esiste. Nessuna delle 5 implementazioni esistenti si chiama `graph_alist`. Il file non è utilizzabile senza prima creare o rinominare un modulo.

## Dati

- Formato TSPLIB standard: sezioni `NAME`, `DIMENSION`, `EDGE_WEIGHT_TYPE`, `NODE_COORD_SECTION`, `EDGE_WEIGHT_SECTION`, etc.
- Weight type supportati: `EXPLICIT` (con `LOWER_DIAG_ROW` o `UPPER_ROW`), `ATT` (coordinate euclidee), `EDGE_LIST`
- I file `.opt.tour` contengono la soluzione ottima nota

## Verifica

Non esiste un test automatico. Per verificare: eseguire lo script con `uv run python <path>`.
