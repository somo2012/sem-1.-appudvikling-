m=['p','r','o','g','r','a','m','m','e','r','i','n','g',' ','e','r',' ',
'b','e','r','u','s','e','n','d','e']
print(m[10],m[17],m[5]) 
#printet skriver I B A og bliver skrevet fordi det tallene i print kommandoen er index pladsen i listen
print(m[-16],m[-9],m[-21])
#samme som før nu køre vi bare baglæns da index tallene er negative.

# opgave 2 opret list og print den tilføj så element
l=[1,2,3,4]
print(l)
l.append(6)
print(l)

#opgave 3 Forklar hvad l.insert(2,3) gør ved din liste 
l.insert(2,3)  # den insætter l.insert(plads i,x)  x element på plads i listen 
print(l)

#Opgave 4
# Skriv l.pop(0). Hvad sker der med din liste?
l.pop(0)  # den fjerner elementet på index 0s plads og alle andre bliver rykket frem?
print(l)  

#  Opgave 5
#Der er mange flere list-operationer. L er en liste og x et element. Prøv nedenstående operationer af:
#  l.extend(L)  , l.remove(x)  , l.index(x)  , l.count(x)  , l.reverse()
l.remove(6) # fjerner 6 fra vores liste
l.index(4) # finder index for givne element på listen
l.count(3) # tæller hvor mange gange dit element går igen
l.reverse() # vender listen om

print(l,  'count :', l.count(3), 'index : ',  l.index(4)    )



#Opgave 6
#Skriv kode, der giver en liste med kvadrattallene af en anden liste.
#Eksempel: input [1,2,4,5] giver output [1,4,16,25].
#Hint: Brug en for-løkke.
op6_liste=[1,2,4,5]
lenght=int(len(op6_liste))
for lenght in (op6_liste):
    print(lenght)








#Opgave 7
#a) Lav en liste med alle ulige tal op til 10.
#b) Lav en liste med alle ulige tal op til n, hvor n er et vilkårligt t
talliste=[1,2,3,4,5,6,7,8,9,10]
uligetals= talliste[0:10:2]

nuligetal= uligetals= talliste[0::2]
print(uligetals,nuligetal)