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