# 🔗 One-Pass Removal of k-th Node from End

Soluzione algoritmica per eliminare un nodo a una distanza specifica dalla coda di una **Singly Linked List** in un unico attraversamento, ottimizzando le prestazioni ed evitando conteggi multipli.

---

## 📝 Descrizione del Problema
Data la testa (`head`) di una lista concatenata singola e un intero **k**, l'obiettivo è rimuovere il nodo che si trova alla posizione **k** contando dalla fine della lista (dove `k = 0` è l'ultimo nodo).

### Regole di Output:
* **Ritorna la Nuova Testa**: Il risultato deve essere il puntatore al primo nodo della lista modificata.
* **Validità di k**: Se **k** è fuori dai limiti della lista (es. negativo o maggiore della lunghezza), la funzione deve restituire la lista originale intatta.
* **One-Pass**: La rimozione deve avvenire attraversando la lista **una sola volta**.

### 💡 Esempi
| Input (`head`) | Valore `k` | Spiegazione | Risultato |
| :--- | :--- | :--- | :--- |
| `[5, 6, 7, 8]` | `3` | Il 4° nodo dalla fine (indice 0) è il 5. | `[6, 7, 8]` |
| `[1, 5]` | `0` | Il 1° nodo dalla fine è l'ultimo (il 5). | `[1]` |
| `[10, 20]` | `5` | Errore: `k` è maggiore della lunghezza della lista. | `[10, 20]` |

---

## 🧠 Approccio e Soluzione

Per risolvere il problema in un unico passaggio, utilizziamo la **Tecnica dei due Puntatori** (o tecnica del "corridore"), che permette di misurare una distanza senza conoscere la lunghezza totale della lista.

### 1. La Strategia del Distacco Fisso
In una lista singola non possiamo tornare indietro. Il segreto è creare un "distacco" di **k** passi tra due puntatori, che chiameremo **x_veloce** e **x_lento**. Quando il puntatore veloce raggiunge il traguardo (la fine della lista), quello lento si troverà esattamente dove ci serve.

* **Complessità Temporale**: O(n), dove n è il numero di nodi (visitiamo ogni nodo una sola volta).
* **Complessità Spaziale**: O(1), poiché utilizziamo solo due puntatori di supporto indipendentemente dalla dimensione della lista.

### 2. Algoritmo di Rimozione
L'algoritmo esegue i seguenti passaggi fondamentali usando la logica dei puntatori **x**:

1. **Anticipo (Offset)**: Si muove il puntatore **x_veloce** in avanti per **k** volte.
2. **Verifica della Testa**:
    * Se dopo i passi **x_veloce** è `None`, `k` non era valido.
    * Se invece `x_veloce.next` è `None`, significa che dobbiamo rimuovere proprio la **testa** della lista. Ritorniamo `head.next`.
3. **Avanzamento Sincronizzato**: Si muovono sia **x_veloce** che **x_lento** di un passo alla volta finché **x_veloce.next** non diventa `None`.
4. **Il Salto (Rimozione)**: 
    * A questo punto, **x_lento** si trova sul nodo **precedente** a quello da eliminare.
    * Si esegue `x_lento.next = x_lento.next.next`, escludendo il nodo target dalla catena.

> **Nota Tecnica**: Questa soluzione è estremamente efficiente per sistemi ad alte prestazioni perché evita di dover scorrere la lista due volte (una per contare e una per eliminare), riducendo il tempo di esecuzione della metà.