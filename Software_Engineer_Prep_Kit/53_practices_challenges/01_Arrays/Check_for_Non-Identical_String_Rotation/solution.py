"""
CHALLENGE: "Non-Identical String Rotation"
1. Escludiamo i casi banali: se le lunghezze differiscono o le stringhe sono 
   identiche, non può esserci una rotazione (ritorna 0).
2. Sfruttiamo s1 + s1: questa stringa contiene tutte le possibili 
   rotazioni di s1 come sottostringhe.
3. Usiamo x come indice per scorrere ogni possibile punto di inizio in s_tot.
4. Per ogni x, verifichiamo se i caratteri successivi corrispondono a s2:
   - Se un carattere non coincide, usiamo 'break' per passare subito alla 
     posizione x successiva (efficienza).
   - Se completiamo il ciclo interno senza interruzioni, abbiamo trovato 
     la rotazione, allora match= True (ritorna 1).
"""
def isNonTrivialRotation(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    
    if n2!=n1 or s1==s2:
        return 0
        
    s_tot=s1+s1
    
    for i in range(n1):
        match = True
        for j in range(n1):
            if s_tot[i+j]!=s2[j]:
                match= False
                break #interrompe il ciclo interno con indice j
        if match:
            return 1
        
    return 0