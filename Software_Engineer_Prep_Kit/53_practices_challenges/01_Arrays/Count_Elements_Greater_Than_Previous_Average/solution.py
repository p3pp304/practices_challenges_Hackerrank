"""============================================================================
LOGICA:
L'algoritmo attraversa l'array una sola volta. Per ogni iterazione:
1. La variabile responseTimes(i) rappresenta l'elemento corrente.
2. Viene mantenuta una somma(parziale) di tutti gli elementi precedenti.
3. Si confronta responseTimes(i) con la media (somma / i).
4. Se responseTimes(i) > media, si incrementa il contatore dei risultati.

NOTE TECNICHE:
- In Python 3 la divisione '/' è float di default, quindi la precisione è 
  mantenuta senza casting espliciti.
- Ottimizzazione: (responseTimes(i) * i > somma_parziale) evita del tutto la divisione.

COMPLESSITÀ:
- Time Complexity: O(n) - Un solo ciclo attraverso l'array.
- Space Complexity: O(1) - Memoria costante, non servono array ausiliari.
============================================================================"""

def countResponseTimeRegressions(responseTimes):
    if not responseTimes:
        return 0
    n= len(responseTimes)
    somma=responseTimes[0]
    count=0
    for i in range(1,n):
        media=somma/i
        if responseTimes[i]>media:
            count+=1
        somma+=responseTimes[i]
    return count