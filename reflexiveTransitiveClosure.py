import numpy as np
import itertools

 ##   ALGORITHM ONE       ##
def algorithmOne(matrixR,listA):
    RKleene = set()

    #This will create all possible tuples of given length
    def findTuples(index, listA):
        tupleOfIndex = set()
        for element in itertools.product(listA, repeat=index):
            tupleOfIndex.add(element)
        return list(tupleOfIndex)

    
    for index in range(len(listA)):
        tupleLength = index+1
        
        for tuple in findTuples(tupleLength,listA):
            #If the length is one, make it reflexive and add to RKleene.
            if tupleLength == 1: 
                RKleene.add((tuple[0], tuple[0]))
            elif tupleLength == 2:
                if (tuple[0], tuple[1]) in matrixR:
                    RKleene.add((tuple[0], tuple[1]))
            else:
                comparingIndex = 0
                done = False
                
                while comparingIndex+1 != tupleLength:
                    #Look if tuples exist in R*
                    if (tuple[comparingIndex], tuple[comparingIndex+1]) in RKleene:
                        if comparingIndex+1 == tupleLength - 1:
                            done = True
                            break
                        comparingIndex += 1
                        
                    # it breaks the path
                    else:
                        break
                if done:
                    RKleene.add((tuple[0], tuple[tupleLength - 1]))

    print("The reflexive transitive closure R*:\n ",np.array(list(RKleene)))

    
    
 ##   ALGORITHM TWO     ##    
def algorithmTwo(matrixR,listA):
  # Initially R*: R U {(ai,ai) : ai∈A^2 (Makes R* Reflexive)
    RKleene = matrixR
    for e in listA: 
        newrow = [e,e]
        if(newrow not in RKleene.tolist()):
            RKleene = np.vstack([RKleene,newrow])
            
    i,j,k= 0,0,0
    #With while,everytime there is a new (ai,ak) it will search again.
    while(i < len(listA)):
        j=0
        while (j < len(listA)):
            k=0
            while(k < len(listA)):
                check1 = [listA[i],listA[j]] in RKleene.tolist() 
                check2 = [listA[j],listA[k]] in RKleene.tolist()
                check3 = [listA[i],listA[k]] in RKleene.tolist()
                if( check1 and check2 and (not check3)):
                    newrow = [listA[i],listA[k]]
                    RKleene = np.vstack([RKleene,newrow])
                    i,j,k = 0,0,0
                else:
                    k+=1
            j+=1               
        i+=1
        
    print("The reflexive transitive closure R*:\n ",RKleene)
    
    
   ##   ALGORITHM THREE     ##
def algorithmThree(matrixR,listA):
    # Initially R*: R U {(ai,ai) : ai∈A^2 (Makes R* Reflexive)
    RKleene = matrixR
    for e in listA: 
        newrow = [e,e]
        if ( (newrow in RKleene.tolist()) == False):
            RKleene = np.vstack([RKleene,newrow])

    for j in range(len(listA)):
        for i in range(len(listA)):
            for k in range(len(listA)):
                check1 = [listA[i],listA[j]] in RKleene.tolist() 
                check2 = [listA[j],listA[k]] in RKleene.tolist()
                check3 = [listA[i],listA[k]] in RKleene.tolist()

                #Look if (ai,aj),(aj,ak)∈ R* but (ai,ak)∉ R* 
                if (check1 and check2 and (check3==False)):
                    addRow = [listA[i],listA[k]]
                    RKleene = np.vstack([RKleene, addRow]) # Add (ai,ak) to R* (Makes R* Transitive)
                                                    
    print("The reflexive transitive closure R*:\n ",RKleene) 


def takeInputR():
    R = int(input("Enter the number of rows of R: ")) 
    C = 2

    matrixR = []
    print("Enter your R. If its R={(a,b),(b,c)}, input it in this format:\na,b\nb,c") 
    matrixR = [list(map(str,input().split(','))) for i in range(R)]
    print("Your R = ",matrixR)
    return matrixR

def takeInputA():
    inputElements = input("Enter the elements of A, seperate each element by comma. \n")
    listA = inputElements.split(',')
    print("Your A = ",listA)
    return listA

checkLoop = True 
while (checkLoop):
    choose = int(input("Which Algorithm do you want to use?\nPress 1 for first, 2 for second and 3 for third:\n"))
     
    if choose == 1:
        algorithmOne(list(set(map(tuple,takeInputR()))),takeInputA())
        checkLoop = False
    elif choose == 2:
        algorithmTwo(np.array(takeInputR()),takeInputA())
        checkLoop = False
    elif choose == 3:
        algorithmThree(np.array(takeInputR()),takeInputA())
        checkLoop = False
    else:
        print("You should press 1,2 or 3.")
