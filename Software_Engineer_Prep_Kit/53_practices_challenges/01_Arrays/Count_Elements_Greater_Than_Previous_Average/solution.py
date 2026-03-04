"""============================================================================
 * CHALLENGE: Count Elements Greater Than Previous Average
 * ============================================================================
LOGICA:
L'algoritmo attraversa l'array una sola volta. Per ogni iterazione:
1. La variabile responseTimes(i) rappresenta l'elemento corrente.
2. Viene mantenuta una somma(parziale) di tutti gli elementi precedenti.
3. Si confronta responseTimes(i) con la media (somma / i).
4. Se responseTimes(i) > media, si incrementa il contatore dei risultati.

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