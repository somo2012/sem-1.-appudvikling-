vare= ["kattebakke", "kattemad", "kredsetræer", "killingelegetøj"] # de enkelte varer 
lager = ["100", "120", "80","60"] #Lagerbeholdning for hver vare

#funktioner
def lagerbeholdning(vare,lager):
  for i in range(len(vare)):
 
    print(vare[i], '\t ' , lager[i]"på lager")

def købvare(vare,lager):
    if input =="køb":
          print(input("hvilken vare?")) # vælg den enkelte vare
          print(input int("hvor mange skal du have?"))
    else:
          print(lagerbeholdning,)


        
  
#interface 
print ("vælg din handling",
"1- køb vare",
"2- lagerbeholdning",
"3- afslut")



# list med vare og lagerbeholdning

print("vare - beholdning")
for i in range(len(vare)):
 
    print(vare[i], '\t ' , lager[i])

# tjek om der er nok på lager
if lager > input(): 
    print ("lagt i kurv")

else: 
    print ("ikke nok på lager")




