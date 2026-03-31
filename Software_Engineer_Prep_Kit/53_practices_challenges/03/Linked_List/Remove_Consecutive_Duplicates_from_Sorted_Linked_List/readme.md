# 🔗 Remove Consecutive Duplicates from Sorted Linked List

Soluzione algoritmica per eliminare tutti i nodi duplicati in una **Singly Linked List** ordinata, mantenendo solo la prima occorrenza di ogni valore e ottimizzando l'uso della memoria tramite la modifica in-place.

---

## 📝 Descrizione del Problema
Data la testa (`head`) di una lista concatenata singola i cui valori sono ordinati in modo non decrescente, l'obiettivo è rimuovere i nodi in eccesso in modo che ogni numero compaia esattamente una sola volta all'interno della catena.

### Regole di Output:
* **Ritorna la Nuova Testa**: Il risultato deve essere il puntatore al primo nodo della lista deduplicata (che rimane invariato rispetto all'originale).
* **Modifica In-Place**: Non devono essere create nuove liste o istanziati nuovi nodi; i collegamenti della struttura originale devono essere modificati direttamente.
* **Adiacenza Garantita**: Poiché la lista è già ordinata, è matematicamente garantito che i nodi con lo stesso valore si trovino l'uno immediatamente accanto all'altro.

### 💡 Esempi
| Input (`head`) | Spiegazione | Risultato |
| :--- | :--- | :--- |
| `[1, 1, 2]` | Il valore 1 è duplicato. Ne manteniamo solo il primo. | `[1, 2]` |
| `[1, 2, 2, 2, 3]` | Il valore 2 è ripetuto tre volte. Saltiamo i due nodi extra. | `[1, 2, 3]` |
| `[]` | Lista vuota, nessun elemento da processare. | `[]` |

---

## 🧠 Approccio e Soluzione

Per risolvere il problema, utilizziamo la tecnica del **Single-Pointer Traversal**. Sfruttiamo il fatto che la lista è ordinata per confrontare in modo iterativo ogni nodo esclusivamente con il suo immediato vicino.

### 1. La Strategia del Bypass In-Place
Invece di allocare un array temporaneo o una struttura dati set per tenere traccia dei numeri visti, ci limitiamo a "scollegare" i duplicati dalla catena logica della lista, reindirizzando agilmente i puntatori.

* **Complessità Temporale**: O(n), dove n è il numero di nodi. L'algoritmo visita ogni nodo al massimo una volta.
* **Complessità Spaziale**: O(1), poiché modifichiamo i collegamenti direttamente in memoria utilizzando un singolo puntatore di supporto, indipendentemente da quanto sia lunga la lista.

### 2. Algoritmo di Rimozione
L'algoritmo esegue i seguenti passaggi fondamentali usando la logica del puntatore **x**:

1. **Inizializzazione**: Si posiziona il puntatore **x** sulla `head` della lista.
2. **Controllo di Sicurezza**: L'attraversamento procede solo se **x** e il suo vicino **x.next** esistono (`while x and x.next`). Questo previene istantaneamente errori fatali su liste vuote o arrivati all'ultimo nodo.
3. **Confronto ed Eliminazione (Il Taglio)**:
    * Si valutano i dati (`x.data == x.next.data`). Se corrispondono, abbiamo individuato un duplicato.
    * Si esegue il bypass: `x.next = x.next.next`. Il nodo corrente salta il duplicato e si aggancia al nodo ancora successivo. 
    * *Attenzione:* In questo caso **x** non avanza! Rimane fermo per verificare se il nuovo nodo appena agganciato è un ulteriore duplicato.
4. **Avanzamento**:
    * Se i valori sono diversi, la sequenza di duplicati si è interrotta. Si può quindi spostare il puntatore in avanti in sicurezza: `x = x.next`.

> **Nota Tecnica**: Questa soluzione è estremamente elegante perché, oltre a consumare zero risorse supplementari, sfrutta il Garbage Collector del linguaggio per pulire in automatico la memoria dai nodi "orfani" (quelli che sono stati bypassati e non sono più raggiungibili dalla catena principale).

---

