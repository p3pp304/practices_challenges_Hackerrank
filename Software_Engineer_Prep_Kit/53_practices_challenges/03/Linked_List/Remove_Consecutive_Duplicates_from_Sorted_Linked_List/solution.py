"""
 * ============================================================================
 * CHALLENGE: Remove Consecutive Duplicates from Sorted Linked List
 * ============================================================================
 * LOGICA (Single-Pointer Traversal / Modifica In-Place):
 * L'obiettivo è eliminare tutti i nodi duplicati in una lista concatenata
 * già ordinata, mantenendo solo la prima occorrenza di ogni valore.
 * Poiché la lista è ordinata, i nodi con lo stesso valore sono sempre adiacenti.
 *
 * 1. STRUMENTI (Un Singolo Puntatore):
 * - Si utilizza un solo puntatore, 'x', che parte dalla testa (head) della 
 * Singly Linked List.
 * - Perché? Essendo i duplicati consecutivi, non abbiamo bisogno di inseguitori.
 * Ci basta confrontare il nodo in cui ci troviamo ('x') con il suo immediato 
 * vicino ('x.next').
 *
 * 2. PROCESSO DI ESECUZIONE:
 * - FASE 1 (Sicurezza / Limiti): Il ciclo 'while x and x.next' assicura 
 * che ci fermiamo prima di cadere fuori dalla lista. Se 'x' è l'ultimo nodo,
 * non ha un vicino con cui confrontarsi.
 * - FASE 2 (Confronto Esplicito): Valutiamo i dati contenuti nei nodi
 * (x.data == x.next.data), non gli oggetti in memoria.
 * - FASE 3 (Bypass / Taglio): Se troviamo un duplicato, "scolleghiamo" il 
 * nodo successivo reindirizzando il puntatore: x.next = x.next.next.
 * [!] ATTENZIONE: Durante questo passaggio, 'x' NON avanza. Il nuovo nodo 
 * appena agganciato potrebbe infatti essere un ulteriore duplicato.
 * - FASE 4 (Avanzamento): Se i valori sono diversi, abbiamo confermato che 
 * il nodo successivo è distinto. Possiamo finalmente spostare in sicurezza 
 * il nostro puntatore in avanti: x = x.next.
 """
 
def deleteDuplicates(head):
    temp=head
    while temp and temp.next:
        if temp.next.data==temp.data:
            temp.next=temp.next.next
        else:
            temp=temp.next
    return head