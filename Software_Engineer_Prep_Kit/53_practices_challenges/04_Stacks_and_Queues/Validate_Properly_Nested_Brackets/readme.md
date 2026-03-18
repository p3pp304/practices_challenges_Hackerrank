# 📥 Validate Properly Nested Brackets (Validazione Parentesi)

Soluzione algoritmica per verificare l'integrità e il corretto annidamento delle parentesi in una stringa di codice o testo, garantendo la coerenza strutturale.

---

## 📝 Descrizione del Problema
Data una stringa `code_snippet` composta da caratteri ASCII, l'obiettivo è determinare se tutte le tipologie di parentesi presenti — tonde `()`, quadre `[]` e graffe `{}` — sono chiuse correttamente e nell'ordine in cui sono state aperte.

### Regole di Output:
* **Ritorna un Booleano (1/0)**: Ritorna **1** se la stringa è valida, **0** se è presente un errore di chiusura o annidamento.
* **Stringa Vuota**: Una stringa senza parentesi o vuota è considerata valida (**1**).

### 💡 Esempi
| Input (`code_snippet`) | Spiegazione | Risultato |
| :--- | :--- | :--- |
| `if (a[0] > b[1]) { }` | Ogni apertura ha la sua chiusura nel giusto ordine. | **1** |
| `([)]` | Errore: `]` chiude prima che venga chiusa la tonda `(`. | **0** |
| `(( )) ]` | Errore: C'è una chiusura quadra senza un'apertura precedente. | **0** |

---

## 🧠 Approccio e Soluzione

Per risolvere il problema con un'efficienza ottimale, utilizziamo la **Strategia LIFO** (*Last In, First Out*) tramite l'uso di una **Pila (Stack)**.

### 1. Il concetto di "Stack-Based Validation"
Il segreto è mantenere memoria delle parentesi ancora aperte. L'ultima parentesi aperta è sempre la prima che deve essere chiusa.



* **Complessità Temporale**: $O(n)$, dove $n$ è la lunghezza della stringa (eseguiamo un singolo ciclo).
* **Complessità Spaziale**: $O(n)$ nel caso peggiore (tutte parentesi aperte), per memorizzare gli elementi nella pila.

### 2. Algoritmo di Controllo
L'algoritmo esegue i seguenti passaggi fondamentali:
1. **Inizializzazione**: Viene creata una lista vuota `pila` che fungerà da stack.
2. **Ciclo di Scansione**: Si analizza ogni carattere **x** della stringa:
    * **Apertura**: Se **x** è `(`, `[` o `{`, viene aggiunto in cima alla pila tramite `.append()`.
    * **Chiusura**: Se **x** è `)`, `]` o `}`:
        1. Si verifica se la pila è vuota (errore: chiusura senza nessuna apertura).
        2. Si estrae l'ultimo elemento della pila con `.pop()` (ultima apertura) e lo si confronta con la chiusura corrente. Se apertura e chiusura non presentano lo stesso tipo di parentesi, avremo errore (**return 0**).
3. **Verifica Finale**: 
    * Se alla fine del testo la pila è **vuota**, tutte le parentesi sono state bilanciate correttamente.
    * Se la pila contiene ancora elementi, significa che mancano delle chiusure.
