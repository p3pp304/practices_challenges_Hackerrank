"""
 * ============================================================================
 * CHALLENGE: Find First Occurrence
 * ============================================================================
 * LOGICA (Ricerca Binaria + Scansione di Sicurezza):
 * L'obiettivo è trovare il primo indice di un target in un array ordinato con 
 * possibili duplicati, evitando errori di indice fuori dai limiti.
 * 1. Si utilizza la ricerca binaria standard per trovare il valore target.
 * 2. Una volta trovato (nums[mid] == target), si avvia un ciclo 'while'.
 * 3. Il ciclo si sposta a sinistra (mid = mid - 1) finché i valori sono uguali,
 * ma solo finché l'indice è valido (mid >= 0).
 * 4. Si restituisce mid + 1 per compensare l'ultimo decremento del ciclo.
 * ============================================================================
"""
def findFirstOccurrence(nums, target):
    n= len(nums)
    low=0
    high=n-1
    
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            while nums[mid]==target and mid>=0:
                mid=mid - 1
            return mid+1
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
            
    return -1