# Count Elements Greater Than Previous Average

Questo esercizio consiste nel determinare quanti elementi in una sequenza temporale sono strettamente superiori alla media di tutti i valori che li hanno preceduti.

## 📝 Descrizione del Problema
Dato un array di interi positivi, il compito è restituire il numero di elementi che sono **strettamente maggiori** della media di tutti gli elementi precedenti. Il primo elemento viene sempre saltato poiché non ci sono elementi precedenti con cui confrontarlo.

## 💡 Esempio
**Input:** `responseTimes = [100, 200, 150, 300]`

**Output:** `2`

**Spiegazione:**
* **Giorno 0:** `100` (nessun giorno precedente, salta).
* **Giorno 1:** `200` > media(100) = 100 → **x** = 1.
* **Giorno 2:** `150` vs media(100, 200) = 150 → non è maggiore → **x** = 1.
* **Giorno 3:** `300` > media(100, 200, 150) = 150 → **x** = 2.
* **Risultato Finale:** `2`.

---

## 🧠 Approccio e Ottimizzazione
Per risolvere questo problema in modo efficiente, evitiamo di ricalcolare la somma degli elementi da zero a ogni passaggio, operazione che porterebbe a una complessità quadratica ($O(n^2)$).

Utilizziamo invece una **somma parziale (running sum)**:
1. Manteniamo una variabile per la somma di tutti gli elementi visti finora.
2. Usiamo la variabile **x** per memorizzare il conteggio degli elementi che soddisfano la condizione.
3. Ad ogni iterazione `i` (partendo da 1):
    * Calcoliamo la media precedente dividendo la somma accumulata per `i`.
    * Se l'elemento corrente è maggiore della media, incrementiamo **x**.
    * Aggiorniamo la somma aggiungendo l'elemento corrente per il ciclo successivo.

