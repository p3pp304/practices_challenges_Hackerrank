"""
 * ============================================================================
 * CHALLENGE: Maximum Non-Overlapping Intervals (Scheduling)
 * ============================================================================
 * LOGICA (Greedy Strategy - Earliest End Time):
 * L'obiettivo è selezionare il maggior numero di intervalli che non si
 * sovrappongono, massimizzando l'occupazione della risorsa.
 * * 1. ORDINAMENTO: Si ordina l'array in base all'orario di fine (indice 1).
 * - Perché? Chi finisce prima libera lo spazio per nuovi incontri.
 * - Usiamo un 'Selection Sort' manuale cercando l'indice 'min_ind'.
 * * 2. SELEZIONE GREEDY:
 * - Si sceglie sempre il primo incontro della lista ordinata.
 * - Si tiene traccia del termine dell'ultimo incontro scelto ('last_end').
 * - Per ogni incontro successivo, lo si include solo se il suo orario
 * di inizio è maggiore o uguale a 'last_end'.
 * ============================================================================
"""
def maximizeNonOverlappingMeetings(meetings):
    n=len(meetings)
    if n==0:
        return 0
    
    for i in range(n):
        min_ind=i
        for j in range (i+1,n):
            if meetings[j][1]<meetings[min_ind][1]:
                min_ind=j
        meetings[i],meetings[min_ind]=meetings[min_ind],meetings[i]
        
        last_end=meetings[0][1]
        count=1
        for i in range(1,n):
            if last_end<=meetings[i][0]:
                count+=1
                last_end=meetings[i][1]
                
    return count