# 🔍 Binary Search (Ricerca Binaria)

Soluzione algoritmica per individuare l'indice di un elemento in un array ordinato con efficienza logaritmica.

---

## 📝 Descrizione del Problema
Dato un array di interi `nums` **ordinato** in modo crescente e un valore `target`, l'obiettivo è determinare l'indice del `target` all'interno dell'array.

### Regole di Output:
* **Ritorna l'indice**: Se il `target` è presente nell'array.
* **Ritorna -1**: Se il `target` non è presente nell'array.

### 💡 Esempi
| Array (nums) | Target | Risultato | Note |
| :--- | :--- | :--- | :--- |
| `[-1, 0, 3, 5, 9, 12]` | `9` | **4** | Il target si trova all'indice 4. |
| `[1, 2, 5, 10]` | `1` | **0** | Il target si trova all'indice 0. |
| `[1, 2, 5, 10]` | `3` | **-1** | Il target non è presente. |

---

## 🧠 Approccio e Soluzione

Per risolvere il problema rispettando il vincolo di tempo **$O(\log n)$**, utilizziamo la strategia del **dimezzamento** (divide et impera).

### 1. Il concetto di dimezzamento
Invece di controllare ogni elemento (ricerca lineare), l'algoritmo confronta il `target` con l'elemento centrale dell'array. Se non c'è corrispondenza, metà dell'array viene scartata ad ogni passaggio.
* **Esempio:** In un array di 1024 elementi, bastano al massimo 10 confronti per trovare il valore o confermare che non esiste.



[Image of binary search algorithm diagram]


### 2. Algoritmo di confronto (Variabile x)
L'algoritmo esegue i seguenti passaggi:
1. Definisce due puntatori: `low` (inizio) e `high` (fine dell'array).
2. Utilizza un ciclo `while` che continua finché `low <= high`.
3. Ad ogni iterazione, calcola il punto medio e lo assegna alla variabile **x** (o `mid`).
4. Confronta `nums[x]` con il `target`:
    * Se coincidono, restituisce **x**.
    * Se `nums[x] < target`, scarta la metà sinistra impostando `low = x + 1`.
    * Se `nums[x] > target`, scarta la metà destra impostando `high = x - 1`.
