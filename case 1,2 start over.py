vare= ["kattebakke", "kattemad", "kredsetræer", "killingelegetøj"] # de enkelte varer 
lager= [int("100"), int("120"), int("80"),int("60")] #Lagerbeholdning for hver vare

#funktioner

#funktion til at printe lagerbeholdningen (vare,lager)
def lagerbeholdning():
 for i in range(len(vare)):
    print(vare[i],'\t       ', lager[i],"på lager")
     
#funktion til salg
def salg():
  while True:
    lagerbeholdning()
    valgt_vare =input("tast varenavn ind (eller skriv 'stop' for at afslutte):")
    if valgt_vare== 'stop':
      break

    if valgt_vare =='kattebakke':
      køb0=int(input("hvor mange vil du købe?"))
      if køb0 <= lager[0]:
        lager.insert(0, lager[0]-køb0)
        print("Du har købt. ", køb0)
      else:
        print("Ikke nok på lager. ")
    

    if valgt_vare == 'kattemad' :
      køb1=int(input("hvor mange vil du købe?"))
      if køb1 <= lager[1]:
        lager.insert(1, lager[1]-køb1)
        print("Du har købt. ", køb1)
      else:
        print("Ikke nok på lager. ")

    elif valgt_vare == "kredsetræer":
      køb2=int(input("hvor mange vil du købe?"))
      if køb2 <= lager[2]:
        lager.insert(2, lager[2]-køb2)
        print("Du har købt. ", køb2)
      else:
        print("Ikke nok på lager. ")

    elif valgt_vare == "killingelegetøj":
      køb3=int(input("hvor mange vil du købe?"))
      if køb3 <= lager[3]:
        lager.insert(3, lager[3]-køb3)
        print("Du har købt. ", køb3)
      else:
        print("Ikke nok på lager. ")
    else: 
      print ("ugyldigt valg prøv igen")

#funktion til vareopfyldning 
def vareopflydning():
  for i in range(len(vare)):
    lagerbeholdning()
    valgt_vare =input("tast varenavn ind for at genopfylde valgte skriv'alle' for at fylde hele lageret op(eller skriv 'stop' for at afslutte):")
    if valgt_vare== 'stop':
      break

    elif valgt_vare =='kattebakke':
      køb0=int(input("hvor mange vil du tilføje?"))
      lager.insert(0, lager[0]+køb0)

    elif valgt_vare == 'kattemad' :
      køb1=int(input("hvor mange vil du tilføje?"))
      lager.insert(1, lager[1]+køb1)

    elif valgt_vare == "kredsetræer":
      køb2=int(input("hvor mange vil du tilføje?"))
      lager.insert(2, lager[2]+køb2)


    elif valgt_vare == "killingelegetøj":
      køb3=int(input("hvor mange vil du tilføje?"))
      lager.insert(3, lager[3]+køb3) 

    elif valgt_vare == "alle":  # med en del hjælp fik vi endlig køb til alle op at køre :D 
      køb4=int(input("hvor mange vil du tilføje?"))
      lager[0]=lager[0]+køb4
      lager[1]=lager[1]+køb4
      lager[2]=lager[2]+køb4
      lager[3]=lager[3]+køb4
      print(lager)
    else: 
      print("ugyldigt valg. Prøv igen ")
     
#main hotbar 
def main():
    while True:
        valg = input("\nVælg en handling (1: Salg, 2: Genopfyld, 3: lager, 4: Afslut): ")
        
        if valg == '1':
            salg()
        elif valg == '2':
            vareopflydning()
        elif valg == '3':
            lagerbeholdning()
        elif valg == '4':
            print("Afslutter programmet.")
            lagerbeholdning()
            break
        else:
            print("Ugyldigt valg. Prøv igen.")

if __name__ == "__main__":
    main()