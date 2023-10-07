import math
import random
import time

Array = [random.randint(0, 100) for i in range(15)]
def pogoSort(Array):
    global int
    int=0
    while(testSorted(Array) == False):
        int+=1
        n = len(Array)
        for i in range(0, n):
            j = random.randint(0, n-1)
            Array[i], Array[j] = Array[j], Array[i]
    return Array

def testSorted(Array):
    n = len(Array)
    for i in range(0, n-1):
        if Array[i] > Array[i+1]:
            return False
    return True

# Driver code to test above
time1 = time.time()
print(pogoSort(Array),n)
time2 = time.time()
print((time2-time1)/60)