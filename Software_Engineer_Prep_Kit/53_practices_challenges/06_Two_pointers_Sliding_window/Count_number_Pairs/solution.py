"""
 * ============================================================================
 * CHALLENGE: Count Affordable Number Pairs
 * ============================================================================
 * LOGICA (Nested Loops con Early Exit - O(n^2) Time Complexity):
 * L'obiettivo è contare quante coppie di numeri in un array già ordinato 
 * producono una somma minore o uguale a un budget predefinito.
 * * 1. STRUTTURA DATI E VARIABILI (Cicli Iterativi):
 * - Si utilizzano due indici per scorrere l'array: 'i' (esterno) e 'j' (interno).
 * - Si usa la variabile 'x' per accumulare il conteggio passo dopo passo.
 * * 2. PROCESSO DI RICERCA E CONTEGGIO:
 * - CICLO ESTERNO: Fissa il primo elemento della coppia (prices[i]).
 * - CICLO INTERNO: Valuta tutti gli elementi successivi (prices[j] con j > i).
 * - VERIFICA: Si calcola la somma dei due elementi correnti.
 * * 3. OTTIMIZZAZIONE (Il ruolo del 'break'):
 * - SOMMA VALIDA: Se prices[i] + prices[j] <= budget, incrementiamo 'x' di 1.
 * - SOMMA ECCESSIVA: Se la somma supera il budget, entra in gioco l'ottimizzazione.
 * Essendo l'array ordinato in modo crescente, qualsiasi elemento successivo 
 * a 'j' produrrà una somma ancora più grande. Si usa quindi 'break' per 
 * interrompere immediatamente il ciclo interno e passare al prossimo 'i',
 * risparmiando tempo di calcolo.
 * * 4. CONTROLLO FINALE:
 * - Esauriti i cicli, si ritorna il valore finale di 'x'.
 * ============================================================================
"""

def countAffordablePairs(prices, budget):
    n = len(prices)
    x = 0  # Modificato in x
    
    for i in range(n):
        for j in range(i + 1, n):
            somma = prices[i] + prices[j]
            
            if somma <= budget:
                x += 1
            else:
                break
                
    return x