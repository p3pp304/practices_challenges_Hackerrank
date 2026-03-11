"""
 * ============================================================================
 * CHALLENGE: Validate Properly Nested Brackets
 * ============================================================================
 * LOGICA (Stack-Based Strategy - LIFO-->Last In, First Out):
 * L'obiettivo è verificare che ogni parentesi aperta '(', '[', '{' sia 
 * chiusa correttamente e nell'ordine giusto.
 * * 1. STRUTTURA DATI (Pila):
 * - Si utilizza una lista ('pila') per memorizzare le parentesi aperte.
 * - Perché? L'ultima parentesi aperta deve essere la prima a venire chiusa.
 * * 2. PROCESSO DI VALIDAZIONE:
 * - APERTURA: Se incontriamo una parentesi aperta, la aggiungiamo alla pila.
 * - CHIUSURA: Se incontriamo una parentesi chiusa:
 * a) Verifichiamo se la pila è vuota (chiusura senza apertura -> Errore).
 * b) Estraiamo l'ultimo elemento dalla pila ('pop') e controlliamo 
 * se corrisponde alla versione aperta del carattere corrente.
 * c) Se non corrispondono, l'annidamento è errato -> Ritorna 0.
 * * 3. CONTROLLO FINALE:
 * - Al termine del ciclo, la pila deve essere vuota. Se contiene elementi, 
 * significa che alcune parentesi non sono state chiuse -> Ritorna 0.
 * ============================================================================
"""

def areBracketsProperlyMatched(code_snippet):
    pila=[]
    
    for char in code_snippet:
        if char in ['(','{','[']:
            pila.append(char)
        elif char in [')',']','}']:
            if pila==[]:
                return 0
            if char==')':
                char_inverse='('
            elif char==']':
                char_inverse='['
            else:
                char_inverse='{'
            
            char_inpila=pila.pop()
            if char_inpila!=char_inverse:
                return 0
    
    if len(pila) == 0:
        return 1
    else:
        return 0