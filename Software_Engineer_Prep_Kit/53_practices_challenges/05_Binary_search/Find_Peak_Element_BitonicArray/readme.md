# ⛰️ Find Peak Element in Bitonic Array (Ricerca del Picco in Array Bitonico)

Soluzione algoritmica per individuare rapidamente l'indice dell'elemento massimo (il picco) all'interno di un array con andamento prima crescente e poi decrescente.

## 📝 Descrizione del Problema

Dato un array `counts` di numeri interi che prima aumenta rigorosamente e poi diminuisce rigorosamente (struttura bitonica), l'obiettivo è determinare l'indice in cui si trova il valore massimo.

**Regole di Output:**
* **Ritorna un Intero:** L'indice esatto (0-based) del valore di picco.
* **Vincolo Temporale:** L'algoritmo deve necessariamente essere eseguito con una complessità temporale di O(log n).

## 💡 Esempi

| Array (`counts`) | Spiegazione | Risultato |
| :--- | :--- | :--- |
| `counts = [1, 3, 5, 4, 2]` | Il valore cresce fino a 5 e poi scende. L'indice del 5 è 2. | 2 |
| `counts = [10, 20, 30, 25, 15]` | Il picco massimo è 30, che si trova nella posizione 2. | 2 |

## 🧠 Approccio e Soluzione

Per risolvere il problema senza controllare inutilmente ogni singola posizione sequenzialmente, utilizziamo un approccio basato sulla Ricerca Binaria (Binary Search).

### 1. Il concetto di "Ricerca Binaria su Pendenza"

Invece di testare ciecamente tutti i numeri dall'inizio alla fine (Brute Force puro), sfruttiamo il fatto che l'array ha una struttura a montagna. Analizzando un punto intermedio, possiamo osservare la sua pendenza per capire in quale direzione muoverci. Se il numero successivo è più grande, stiamo salendo e il picco è più avanti; se è più piccolo, stiamo scendendo e il picco si trova indietro (o è la posizione attuale). Possiamo quindi interrompere la ricerca in metà dell'array immediatamente.

* **Complessità Temporale:** O(log n) poiché lo spazio di ricerca si dimezza rigorosamente ad ogni iterazione.
* **Complessità Spaziale:** O(1) poiché non utilizziamo strutture dati aggiuntive, operando direttamente sull'array fornito tramite indici.

### 2. Algoritmo di Selezione

L'algoritmo esegue i seguenti passaggi fondamentali:

1. **Inizializzazione Limiti:** Si definiscono i due puntatori estremi, `low` all'inizio e `high` alla fine dell'array.
2. **Ricerca Centrale:** In un ciclo (finché `low < high`), si individua l'indice `mid` e si salva il suo valore nella variabile `x` (`x = counts[mid]`).
3. **Verifica della Pendenza:**
   * Se `x < counts[mid + 1]`, ci troviamo in fase di salita. Si scarta la metà sinistra spostando `low = mid + 1`.
   * Se `x > counts[mid + 1]`, ci troviamo in fase di discesa o sul picco. Si scarta la metà destra spostando `high = mid`.
4. **Termine del Ciclo:** Quando i puntatori convergono sullo stesso indice, il ciclo si ferma e si ritorna il puntatore finale che indica la posizione esatta della vetta.