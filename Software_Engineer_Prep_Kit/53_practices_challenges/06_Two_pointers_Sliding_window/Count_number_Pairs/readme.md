# 🔢 Count Affordable Number Pairs (Conteggio Coppie Accessibili)

Soluzione algoritmica per contare quante coppie uniche di numeri in un array ordinato producono una somma minore o uguale a un budget predefinito.

---

## 📝 Descrizione del Problema
Dato un array `prices` di numeri interi positivi ordinato in modo non decrescente e un valore target `budget`, l'obiettivo è determinare il numero totale di coppie di indici `(i, j)` tali che `i < j` e **prices[i] + prices[j] <= budget**.

### Regole di Output:
* **Ritorna un Intero**: Il conteggio totale delle coppie valide.
* **Condizione di Validità**: La somma dei due elementi deve rientrare nel budget stabilito.

### 💡 Esempi
| Array (prices) & Budget | Spiegazione | Risultato |
| :--- | :--- | :--- |
| `prices=[1, 2, 3, 4, 5]`, `budget=7` | Coppie valide: (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4). | **8** |
| `prices=[10, 20, 30]`, `budget=15` | Nessuna combinazione rientra nel budget. | **0** |

---

## 🧠 Approccio e Soluzione

Per risolvere il problema senza controllare inutilmente ogni singola combinazione, utilizziamo un approccio basato su **Cicli Annidati con Early Exit** (Uscita Anticipata).

### 1. Il concetto di "Early Exit"
Invece di testare ciecamente tutte le combinazioni possibili (Brute Force puro), sfruttiamo il fatto che l'array è già ordinato. Se `prices[i] + prices[j]` supera il budget, qualsiasi elemento successivo a `j` produrrà una somma ancora più grande. Possiamo quindi interrompere il ciclo interno immediatamente.

* **Complessità Temporale**: $O(n^2)$ nel caso peggiore (es. se tutte le coppie sono valide e non scatta mai il break), ma drasticamente ottimizzata nella pratica per i casi in cui i numeri superano rapidamente il target.
* **Complessità Spaziale**: $O(1)$ poiché non utilizziamo strutture dati aggiuntive, operando direttamente sull'array fornito.

### 2. Algoritmo di Selezione
L'algoritmo esegue i seguenti passaggi fondamentali:
1. **Scorrimento Esterno**: Il ciclo `i` fissa il primo elemento della coppia.
2. **Scorrimento Interno**: Il ciclo `j` (che parte sempre da `i + 1`) cerca il secondo elemento da sommare.
3. **Verifica e Conteggio**:
    * Se la somma è $\leq$ budget, si incrementa la variabile `x` (il nostro contatore).
    * Se la somma è $>$ budget, si attiva il comando `break` per saltare i controlli successivi e passare direttamente al prossimo `i`.

---