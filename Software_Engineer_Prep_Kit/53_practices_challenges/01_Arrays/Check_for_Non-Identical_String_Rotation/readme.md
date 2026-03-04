# 🔄 Non-Identical String Rotation

Soluzione algoritmica per verificare se una stringa è una rotazione non triviale di un'altra.

---

## 📝 Descrizione del Problema
Date due stringhe `s1` e `s2`, l'obiettivo è determinare se `s2` è una rotazione di `s1`, a condizione che `s2` **non** sia identica a `s1`.

### Regole di Output:
* **Ritorna 1**: Se `s2` è una rotazione valida e diversa da `s1`.
* **Ritorna 0**: Se le lunghezze differiscono, se le stringhe sono identiche o se non c'è rotazione.

### 💡 Esempi
| Stringa 1 (s1) | Stringa 2 (s2) | Risultato | Note |
| :--- | :--- | :--- | :--- |
| `"abcde"` | `"cdeab"` | **1** | Rotazione valida. |
| `"apple"` | `"apple"` | **0** | Identiche (non ammesso). |
| `"data"` | `"atad"` | **0** | Non è una rotazione. |
| `"py"` | `"pyth"` | **0** | Lunghezze diverse. |

---

## 🧠 Approccio e Soluzione

Per risolvere il problema in modo efficiente senza spostare fisicamente i caratteri, utilizziamo la strategia della **concatenazione**.

### 1. Il trucco di s_tot
Concatenando `s1` con se stessa (`s_tot = s1 + s1`), generiamo una stringa che contiene al suo interno **tutte le possibili rotazioni** di `s1`. 
*Esempio:* Se `s1 = "abc"`, `s_tot` sarà `"abcabc"`. Le rotazioni possibili (`"bca"`, `"cab"`) sono sottostringhe di questa nuova stringa.



### 2. Algoritmo di confronto (Variabile x)
L'algoritmo esegue i seguenti passaggi:
1. Verifica che `len(s1) == len(s2)` e che `s1 != s2`.
2. Utilizza un ciclo principale con indice **x** per scorrere i punti di inizio in `s_tot`.
3. Per ogni posizione **x**, confronta i caratteri successivi con `s2`.
4. Utilizza l'istruzione `break` per interrompere il confronto interno non appena viene trovata una discrepanza (ottimizzazione).

---

