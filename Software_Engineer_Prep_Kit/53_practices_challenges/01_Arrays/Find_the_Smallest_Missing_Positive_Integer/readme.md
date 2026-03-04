# Find the Smallest Missing Positive Integer
Questo progetto implementa una soluzione efficiente per trovare il più piccolo numero intero positivo (≥ 1) che non è presente in un array non ordinato.

## 📝 Descrizione del Problema
Dato un array di interi non ordinato, l'obiettivo è trovare il più piccolo intero positivo mancante. La soluzione deve essere eseguita in tempo **$O(n)$** e utilizzare uno spazio extra **$O(1)$**.

## 💡 Esempio
**Input:** `orderNumbers = [3, 4, -1, 1]`

**Output:** `2`

**Spiegazione:**
Vogliamo trovare il minimo intero positivo posizionando ogni valore al suo indice corretto (es. il valore `1` all'indice `0`, il valore `2` all'indice `1`, ecc.).
* Inizio: `[3, 4, -1, 1]`
* `i=0`: valore `3` ⇒ scambia con indice `2` ⇒ `[-1, 4, 3, 1]`
* `i=0`: valore `-1` è fuori intervallo (ignora)
* `i=1`: valore `4` ⇒ scambia con indice `3` ⇒ `[-1, 1, 3, 4]`
* `i=1`: valore `1` ⇒ scambia con indice `0` ⇒ `[1, -1, 3, 4]`
* Ora `1` è all'indice `0`, `3` all'indice `2`, `4` all'indice `3`. `-1` rimane all'indice `1`.

Scansione dall'indice `0` usando la variabile **x**:
* **x** = 0: l'indice `0` ha `1` (corretto).
* **x** = 1: l'indice `1` ha `-1` (errato, ci aspettiamo `2`).
⇒ Il minimo intero positivo mancante è **2**.

---

## ⚙️ Specifiche

### Formato Input
1. Un intero `n` nella prima riga ($0 \le n \le 1000$).
2. Le successive `n` righe contengono un intero che rappresenta `orderNumbers[i]`.

### Vincoli
* `0 <= orderNumbers.length <= 1000`
* `-10^9 <= orderNumbers[i] <= 10^9`
* Sono ammessi duplicati.
* Sono ammessi numeri negativi e zero.

---

## 🧠 Approccio e Ottimizzazione (Cyclic Sort)
Per rispettare i vincoli di **$O(n)$** temporale e **$O(1)$** spaziale, non è possibile utilizzare l'ordinamento standard $O(n \log n)$ o un Hash Set ($O(n)$ di spazio).

L'approccio ottimale è il pattern **Cyclic Sort**:
1. Itera attraverso l'array. Se un elemento è un intero positivo minore o uguale alla lunghezza dell'array, scambialo nella sua posizione "corretta" (es. il numero `5` va all'indice `4`).
2. Dopo l'ordinamento, la prima posizione **x** che non contiene il valore **x + 1** indica il numero mancante.
