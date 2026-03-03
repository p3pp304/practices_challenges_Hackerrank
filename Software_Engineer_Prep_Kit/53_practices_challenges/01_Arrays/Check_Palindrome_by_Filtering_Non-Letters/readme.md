# 🔡 Alphabetic Palindrome Checker

Questa funzione determina se una stringa è un **palindromo**, considerando esclusivamente i **caratteri alfabetici** e ignorando completamente la differenza tra **maiuscole e minuscole**.

## 📝 Descrizione del Problema
Data una stringa che può contenere lettere, cifre e simboli, dobbiamo verificare se la sequenza di sole lettere si legge allo stesso modo in avanti e all'indietro.

### Requisiti Specifici:
* **Filtro**: Ignorare cifre, spazi e simboli.
* **Case-Insensitivity**: Trattare 'A' e 'a' come lo stesso carattere.
* **Efficienza**: Ottimizzare il confronto per evitare cicli ridondanti.

---

## 💡 Esempio di Logica
**Input**: `code = "A man, a plan, a canal: Panama"`
* **Filtraggio**: Viene creata la variabile **x** contenente solo le lettere minuscole: `"amanaplanacanalpanama"`.
* **Verifica**: Si confronta la prima lettera con l'ultima, la seconda con la penultima, ecc.
* **Risultato**: `True`.
---

## 🧠 Approccio e Implementazione
L'algoritmo si divide in due fasi principali:

### 1. Fase di Normalizzazione
Invece di gestire la punteggiatura durante il confronto, costruiamo una stringa pulita nella variabile **x**.
* Si itera su ogni carattere della stringa originale.
* Se il carattere è alfabetico (`isalpha()`), viene convertito in minuscolo e aggiunto a **x**.

### 2. Fase di Confronto Simmetrico
Per verificare se **x** è un palindromo, non è necessario invertire l'intera stringa (risparmiando memoria):
* Usiamo la divisione intera `n // 2` per scansionare solo la prima metà della stringa.
* Confrontiamo l'elemento all'indice `i` con quello all'indice `n - 1 - i`.

---

## ⚙️ Specifiche Tecniche

| Proprietà | Dettaglio |
| :--- | :--- |
| **Complessità Temporale** | **O(n)** - Un passaggio per filtrare, uno per controllare. |
| **Complessità Spaziale** | **O(n)** - Per memorizzare la stringa filtrata **x**. |
| **Metodi Utilizzati** | `.isalpha()`, `.lower()`, `len()`. |