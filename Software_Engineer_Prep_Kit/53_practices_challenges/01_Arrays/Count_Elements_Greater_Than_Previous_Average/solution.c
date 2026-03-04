/*
 * ============================================================================
 * CHALLENGE: Count Elements Greater Than Previous Average
 * ============================================================================
 * LOGICA:
 * L'algoritmo attraversa l'array una sola volta. Per ogni iterazione:
 * 1. La variabile x rappresenta l'elemento corrente.
 * 2. Viene mantenuta una 'somma_parziale' di tutti gli elementi precedenti.
 * 3. Si confronta x con la media (somma_parziale / i).
 * 4. Se x > media, si incrementa il contatore dei risultati.
 * ============================================================================
 */

 int countResponseTimeRegressions(int responseTimes_count, int* responseTimes) {
    if (responseTimes_count == 0) {
        return 0;
    }
    int n=responseTimes_count-1;
    double somma=responseTimes[0];
    double average;
    int i;
    int count=0;
    for(i=1;i<=n;i++){
        average=somma/i;
        if(responseTimes[i]>average){
            count++;
        }
        somma+=responseTimes[i];
    }
    return count;
}