"""
 * ============================================================================
 * CHALLENGE: Alphabetic Palindrome Checker
 * ============================================================================
 * LOGICA (Filtro e Confronto Simmetrico):
 * L'obiettivo è verificare se una sequenza di sole lettere è un palindromo,
 * ignorando maiuscole, minuscole, numeri e punteggiatura.
 * 1. Si scorre la stringa originale e, per ogni carattere alfabetico, si
 * aggiunge la sua versione minuscola a una nuova variabile **x**.
 * 2. Si calcola la lunghezza della stringa pulita **x** (chiamata n). Se è
 * vuota, si restituisce False.
 * 3. Si esegue un ciclo fino alla metà della stringa (n // 2), confrontando 
 * il carattere all'indice i con il suo speculare all'indice (n - 1 - i).
 *
 * NOTE TECNICHE:
 * - Costruire la variabile **x** prima del ciclo di verifica evita di 
 * dover gestire indici sfalsati a causa di spazi o simboli ignorati.
 * - L'uso di n // 2 garantisce che il ciclo si fermi al centro esatto,
 * ignorando la lettera centrale nei palindromi dispari (es. "radar").
 * * COMPLESSITÀ:
 * - Time Complexity: **O(n)** - Un passaggio per filtrare i caratteri e 
 * al massimo mezzo passaggio (n/2) per confrontarli.
 * - Space Complexity: **O(n)** - Viene allocata memoria per creare e 
 * memorizzare la stringa filtrata **x**.
 * ============================================================================
"""

def isAlphabeticPalindrome(code):
    x = ""
    for char in code:
        if char.isalpha():
            x += char.lower()
    
    n=len(x)
        
    for i in range(n//2):
        if(x[i]!=x[n-1-i]):
            return False
    return True