import random
import time

def bogoSort(Array):
    global int
    int=0
    while(testSorted(Array) == False):
        int+=1
        if(int%1000000 == 0):
            print(int)
        random.shuffle(Array)
    return Array

def testSorted(Array):
    n = len(Array)
    for i in range(0, n-1):
        if Array[i] > Array[i+1]:
            return False
    return True

tailleArray = 7
timeTotal = time.time()
intTotal = 0
for taille in range (tailleArray-2,tailleArray+1):
    Array = list(range(1,taille+1))
    random.shuffle(Array)
    print(Array)

    # Driver code to test above
    time1 = time.time()
    print(bogoSort(Array))
    print((time.time()-time1))
    print(int)
    intTotal += int

print("Temps total : ", (time.time()-timeTotal), " secondes soit ", (time.time()-timeTotal)/60, " minutes")
print("Nombre total d'itération : ", intTotal)

## Création d'un fichier texte
with open("BogoSort.txt", "w") as fichier :
    ## Ajout dans le fichier
    fichier.write("------ BogoSort ------\n")
    fichier.write("Taille du tableau : "+str(tailleArray)+"\n")
    fichier.write("Nombre total d'itération : "+str(intTotal)+"\n")
    fichier.write("Temps total : "+str((time.time()-timeTotal))+" secondes soit "+str((time.time()-timeTotal)/60)+" minutes\n")