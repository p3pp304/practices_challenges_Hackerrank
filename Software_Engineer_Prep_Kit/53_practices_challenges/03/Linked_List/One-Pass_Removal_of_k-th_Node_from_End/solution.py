"""
 * ============================================================================
 * CHALLENGE: One-Pass Removal of k-th Node from End
 * ============================================================================
 * LOGICA (Two-Pointer Strategy / Tecnica del Corridore):
 * L'obiettivo è eliminare il k-esimo nodo partendo dalla fine della lista
 * in un unico attraversamento (One-Pass), senza prima contarne la lunghezza.
 *
 * 1. STRUMENTI (Due Puntatori):
 * - Si utilizzano due puntatori, 'fast' (veloce) e 'slow' (lento), che 
 * partono entrambi dalla testa (head) della Singly Linked List.
 * - Perché? Creando un "distacco" fisso di k nodi tra i due, quando il primo 
 * tocca il traguardo (la fine), il secondo si troverà esattamente dove serve.
 *
 * 2. PROCESSO DI ESECUZIONE:
 * - FASE 1 (Vantaggio): Spostiamo 'fast' in avanti di k passi.
 * a) Se 'fast' esce dalla lista durante questo ciclo, k è fuori 
 * dai limiti -> Ritorna la lista originale intatta.
 * - FASE 2 (Caso Limite): Se dopo i k passi 'fast' è None, significa che
 * k era esattamente pari alla lunghezza della lista. Il nodo da rimuovere 
 * è quindi la testa -> Ritorna head.next.
 * - FASE 3 (Inseguimento): Muoviamo 'fast' e 'slow' alla stessa velocità
 * (un passo alla volta) finché 'fast' non raggiunge l'ultimo nodo.
 * - FASE 4 (Rimozione): Ora 'slow' si trova ESATTAMENTE sul nodo *precedente*
 * a quello da eliminare. Eseguiamo il "salto" per escluderlo dalla catena: 
 * slow.next = slow.next.next.
 """
 
def removeKthNodeFromEnd(head, k):
    fast=head
    slow=head
    
    for i in range(k):
        if fast.next: 
            fast=fast.next
        else:
            return head
    
    if not fast.next:
        head=head.next
        return head
                   
    while fast.next.next:
        slow=slow.next
        fast=fast.next
        
    slow.next=slow.next.next
    return head
    
    
    