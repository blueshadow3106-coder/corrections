# Ex 3
mot = "Programmation"
#parcours par éléments
for c in mot:
    print(c)
  
#parcours par indices
for i in range(len(mot)):
    print(mot[i])

i = 0
while i < len(mot):
    print(mot[i])
    i = i + 1
    
#Exercice 4
    
def inverse(chaine):
    res = ""
    for i in range(len(chaine)):
        res += chaine[-i-1]
    return res
        
def inverse2(chaine):
    res = ""
    for i in range(len(chaine)):
        res = chaine[i] + res
    return res

#Exercice 5

def positions_lettre(chaine, lettre):
    res = []
    for i in range(len(chaine)):
        if chaine[i] == lettre:
            res.append(i)

    return res
    
#Exo 6
def masquer(mot):
    nv=""
    for i in mot :
        if i in "aeiouy":
            nv=nv+"*"
        else:
            nv=nv+i
    return(nv)
            
#Exo 7
import math
nombres=[5,6,4,2,4]
min=math.inf
max=0
for i in nombres:
    if i>max:
        max=i
    elif i<min:
        min=i
print (max , min)

#Exo 8
nombres=[1,5,8,6,2]
p=[]
im=[]
for i in nombres:
    if (i%2)==0:
        p.append(i)
    else:
        im.append(i)
print(im,p)

#Exo 9 :
def affiche(chaine):
    for i in range(len(chaine)):
        print(i,chaine[i])
    return
