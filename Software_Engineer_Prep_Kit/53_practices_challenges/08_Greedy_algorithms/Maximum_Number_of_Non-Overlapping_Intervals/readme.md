# 📅 Maximum Non-Overlapping Meetings (Pianificazione Incontri)

Soluzione algoritmica per massimizzare il numero di attività eseguibili in una risorsa condivisa, evitando ogni tipo di sovrapposizione temporale. [cite: 2026-02-21]

---

## 📝 Descrizione del Problema
Dato un array 2D `meetings` di dimensioni $n \times 2$, dove ogni riga rappresenta un incontro con un orario di **inizio** e uno di **fine**, l'obiettivo è determinare il numero massimo di intervalli che possono essere completati senza sovrapporsi. [cite: 2026-02-21]

### Regole di Output:
* **Ritorna un Intero**: Il numero totale di riunioni che è possibile incastrare nell'agenda. [cite: 2026-02-21]
* **Condizione di Validità**: Un incontro può iniziare nello stesso istante in cui finisce il precedente ($inizio \geq fine_{precedente}$). [cite: 2026-02-21]

### 💡 Esempi
| Matrice (meetings) | Spiegazione | Risultato |
| :--- | :--- | :--- |
| `[[1,2], [2,3], [3,4], [1,3]]` | Scegliamo [1,2], [2,3] e [3,4]. Scartiamo [1,3]. | **3** |
| `[[0,5], [0,1], [1,2], [2,3]]` | Scegliamo gli incontri brevi per liberare tempo. | **3** |
| `[[5,10]]` | Un solo incontro disponibile. | **1** |

---

## 🧠 Approccio e Soluzione

Per risolvere il problema con un approccio ottimale, utilizziamo la **Strategia Greedy** (algoritmo ingordo) basata sull'orario di termine. [cite: 2026-02-21]

### 1. Il concetto di "Earliest End Time"
Il segreto non è scegliere chi inizia prima, ma chi **libera la stanza** il prima possibile. Scegliendo l'incontro che finisce prima, massimizziamo il tempo residuo per i meeting successivi. [cite: 2026-02-21]

* **Complessità Temporale**: $O(n^2)$ a causa dell'ordinamento manuale (Selection Sort). [cite: 2026-02-21]
* **Complessità Spaziale**: $O(1)$ poiché operiamo direttamente sulla matrice originale senza variabili d'appoggio esterne. [cite: 2026-02-21]



### 2. Algoritmo di Selezione
L'algoritmo esegue i seguenti passaggi fondamentali:
1. **Ordinamento Manuale**: Esegue un ciclo sulla matrice per trovare l'incontro che finisce prima e lo sposta in avanti tramite **Selection Sort**. [cite: 2026-02-21]
2. **Scelta del Pivot**: Inizializza una variabile `last_end` con il tempo di fine del primo incontro ordinato. [cite: 2026-02-21]
3. **Confronto Progressivo**: Scorrendo i restanti incontri, analizza direttamente i valori di inizio e fine senza utilizzare variabili temporanee. [cite: 2026-02-12]
4. **Verifica Sovrapposizione**:
    * Se l'orario di inizio è $\geq$ `last_end`, l'incontro viene accettato. [cite: 2026-02-12, 2026-02-21]
    * Si incrementa il `count` e si aggiorna `last_end` con l'orario di fine dell'incontro corrente. [cite: 2026-02-12, 2026-02-21]

---

