"""
 * ============================================================================
 * CHALLENGE: Find Peak Element in Bitonic Array
 * ============================================================================
 * LOGICA (Ricerca Binaria - O(log n) Time Complexity):
 * L'obiettivo è individuare l'indice del valore massimo in un array bitonico
 * (che prima cresce e poi decresce) nel minor tempo possibile.
 * * 1. STRUTTURA DATI E VARIABILI (Puntatori di Ricerca):
 * - Si utilizzano due puntatori, **low** e **high**, per definire l'intervallo.
 * - Si calcola l'indice **mid** per dividere l'array a metà ad ogni passo.
 * - Si può usare una variabile **x** per memorizzare temporaneamente il valore 
 * in counts[mid] e confrontarlo con il successivo.
 * * 2. PROCESSO DI ANALISI DELLA PENDENZA:
 * - Ad ogni iterazione, si osserva il valore centrale rispetto al suo vicino destro.
 * - SALITA: Se **counts[mid] < counts[mid + 1]**, siamo nella fase crescente.
 * Il picco si trova necessariamente a destra, quindi **low** diventa **mid + 1**.
 * - DISCESA: Se **counts[mid] > counts[mid + 1]**, siamo nella fase decrescente
 * o esattamente sul picco. Il massimo è a sinistra o è il punto attuale,
 * quindi **high** diventa **mid**.
 * * 3. OTTIMIZZAZIONE (Efficienza Logaritmica):
 * - A differenza di una ricerca lineare che controlla ogni elemento, la ricerca 
 * binaria dimezza lo spazio di ricerca ad ogni confronto. 
 * - Questo permette di trovare il picco in un array di un milione di elementi 
 * in soli 20 passaggi circa, rispettando il vincolo **O(log n)**.
 * * 4. CONCLUSIONE E RITORNO:
 * - Il ciclo termina quando **low** e **high** convergono sullo stesso indice.
 * - Si ritorna il valore finale di **low**, che rappresenta l'indice del picco.
 * ============================================================================
 """
 
def findPeakIndex(counts):
    low=0
    high=len(counts)-1
    
    while low<high:
        mid=low + (high-low)//2
        if(counts[mid+1]>counts[mid]):
            low=mid+1
        else:
            high=mid
            
    return low