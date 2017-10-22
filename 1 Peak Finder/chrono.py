from time import time

def chrono(fonction, param):
    #Affichage du nom de la fonction
    print(fonction)
    
    #Calcul du temps 
    tempsStart = time()
    #Appel à la fonction
    resultat = fonction(param)
    #Fin du calcul du temps et retour
    timeSpend = time()-tempsStart
    print ("Temps d'execution = ", timeSpend, "secondes")
    print("---------------------")
    return resultat