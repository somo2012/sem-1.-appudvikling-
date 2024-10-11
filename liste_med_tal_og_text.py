min_liste=['a',1,2,3,4]
print(min_liste)

min_liste.append('b')

min_liste.insert(1, 'to komma fem')
print(min_liste)

#print 3 element
#min_liste[start : stop : hop ]. eksempel  min_liste[0:5] = min_liste[0:5:1]
slice=min_liste[2:3]
print(slice)

#slice af min_liste [start:stop] hvis der ikke er et stop kør til sidste punkt
slice1=min_liste[2:]
print(slice1)

#[start:stop] ikke inkludere sidste
slice2=min_liste[2:4] 
print("slice 2 er ", slice2)

#reverse a list 
# Syntax: reversed_list = min_list[start:stop:step] hvis step sættes til -1 så vil koden går til højeste index og tælle ned derfra
omvendt_liste=min_liste[::-1]
print (omvendt_liste)

#matrix = liste med lister 
matrix=[[1,2], [3,4,5], [5,6]]
print(matrix)
#lister inde i lister håndteres med list[y] [i]  : hvor y er den ydre liste og  i den indre liste indexen i matrixen

matrix.append([9,8,7])
print(matrix)

matrixslice1=matrix [3] [2]

print(matrixslice1)


#lister vs sets vs tupler 

#sets(mængder på dansk) er uordnede samlinger af unikke elementer. fjerner ENS elementer. De bruges til at fjerne dubletter og til matematiske operationer 
#som union() , intersection () , og difference(), sæt har tuborg parenteser rundt om {}

#liste som skal konvertes til set
liste_til_sets= [1,5,2,6,2,6,2,7,1,8]
mit_sæt=set(liste_til_sets)
mit_sæt.add(99)   # tilføj ny element til sættet 
print(mit_sæt)

sæt_2={9,4,4,1}

sæt_2.union(mit_sæt) # læg de to sæt sammen   union/  mængde tegn: U 
sæt_2.intersection(mit_sæt) # hvad sættene har tilfælles    intersection/foreningsmængde 
sæt_2.difference(mit_sæt) # hvad er forskellen fra første set (sæt_2) mellem andet set(mit_sæt)   difference/fraregnet 

print("union", sæt_2.union(mit_sæt))
print('intersection ', sæt_2.intersection(mit_sæt))
print('difference', sæt_2.difference(mit_sæt))


# tupler er uforanderlige(immutable), bruges til faste værdier (da de ikke kan ændres)  tupler bruger runde parenteser
#pakning af tupler giver mulighed for at gruppere værdier sammen.
#og udpakning  bruges til at tildele tuple-værdierne til flere variabler:
#eksempel :
min_tuple= (1,2,'æble')
x,y,z =(1,2,'æble')

print('x,y,z følger :',
      x,
      y,
      z, 
      min_tuple)
print(z, min_tuple)