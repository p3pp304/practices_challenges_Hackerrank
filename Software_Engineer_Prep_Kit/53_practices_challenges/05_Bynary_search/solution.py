"""
 * ============================================================================
 * CHALLENGE: Binary Search
 * ============================================================================
 * LOGICA (Dimezzamento e Confronto Centrale):
 * L'obiettivo è trovare l'indice di un valore 'target' in un array ordinato,
 * riducendo lo spazio di ricerca della metà ad ogni passaggio.
 * 1. Si definiscono i confini iniziali: 'low' (indice 0) e 'high' (n - 1).
 * 2. Finché l'area di ricerca è valida (low <= high), si calcola il punto 
 * medio e lo si assegna alla variabile **mid** (o la nostra variabile **x**).
 * 3. Si confronta il valore all'indice centrale con il target:
 * - Se corrispondono, si restituisce l'indice.
 * - Se il target è maggiore, si scarta la metà sinistra alzando 'low'.
 * - Se il target è minore, si scarta la metà destra abbassando 'high'.
 * ============================================================================
"""
def binarySearch(nums, target):
    n = len(nums)
    low=0
    high=n-1
    
    while low<=high:
        mid=(low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low=mid+1
        else:
            high=mid-1
            
    return -1