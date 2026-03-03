"""
 * ============================================================================
 * CHALLENGE: Find the Smallest Missing Positive Integer
 * ============================================================================
 * LOGICA (Cyclic Sort / In-place Partitioning):
 * L'obiettivo è trovare il minimo intero positivo mancante ottimizzando lo spazio.
 * 1. Si scorre l'array e per ogni elemento x, se x è positivo e rientra nel
 * range dell'array (x <= n), si cerca di spostarlo nell'indice (x - 1).
 * 2. Si scambiano gli elementi finché x non si trova nella sua posizione corretta.
 * 3. In un secondo ciclo, il primo indice i in cui array[i] != i + 1 indica 
 * che il numero mancante è (i + 1).
 *
 * NOTE TECNICHE:
 * - Questo approccio permette di risolvere il problema senza usare una 
 * tabella hash o un array di supporto (booleano).
 * * COMPLESSITÀ:
 * - Time Complexity: O(n) - Anche se c'è un ciclo interno, ogni elemento viene
 * posizionato correttamente al massimo una volta.
 * - Space Complexity: O(1) - Algoritmo "in-place", utilizza l'array originale.
 * ============================================================================
"""

def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)
    i = 0
    
    while i < n:
        x = orderNumbers[i]
    
        if 0 < x <= n and orderNumbers[x - 1] != x:
            orderNumbers[i], orderNumbers[x - 1] = orderNumbers[x - 1], orderNumbers[i]
        else:
            i += 1
            
    for i in range(n):
        if orderNumbers[i] != i + 1:
            return i + 1
    return n+1