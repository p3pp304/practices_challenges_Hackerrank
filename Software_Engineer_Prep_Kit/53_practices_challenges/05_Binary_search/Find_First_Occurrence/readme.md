# 🔍 Find First Occurrence (Pure Binary Search)

Soluzione ottimizzata per trovare l'indice della prima occorrenza di un target in un array ordinato, mantenendo una complessità logaritmica costante.

---

## 📝 Descrizione del Problema
Dato un array `nums` ordinato in modo non decrescente e un valore `target`, individuare il primo indice in cui appare il `target`. Se il valore non è presente, restituire `-1`.

### 💡 Esempio
**Input:** `n=5, target=2`, `nums = [1, 2, 2, 2, 3]`  
**Output:** `1`  

**Spiegazione:** L'algoritmo trova il numero `2` al centro, ma invece di fermarsi, continua a cercare nella metà sinistra per assicurarsi che non ce ne siano altri prima, salvando l'indice migliore trovato finora.

---

## 🧠 Approccio e Soluzione (Ottimizzazione Logaritmica)

A differenza della versione con scansione lineare (`while`), questa soluzione non "cammina" all'indietro, ma continua a dimezzare l'array.



### 1. La variabile `risultato`
Utilizziamo una variabile di supporto (inizializzata a `-1`) per memorizzare l'indice ogni volta che troviamo un valore uguale al `target`.

### 2. Strategia "Cerca ancora a sinistra"
1. Calcoliamo il punto medio **x** (o `mid`).
2. Se `nums[x] == target`:
   * Salviamo l'indice corrente in `risultato`.
   * **Fondamentale:** Continuiamo la ricerca spostando il limite `high = x - 1`. Questo costringe l'algoritmo a vedere se esiste un'altra occorrenza a sinistra.
3. Se `nums[x] < target`: spostiamo `low = x + 1`.
4. Se `nums[x] > target`: spostiamo `high = x - 1`.



