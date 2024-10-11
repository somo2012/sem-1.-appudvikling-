varer = ["kattebakke", "kattemad", "kredsetræer", "killingelegetøj"]
lager = [100, 120, 80, 60]

def vis_lager():
    for i in range(len(varer)):
        print(varer[i], '\t', lager[i], "på lager")

def salg():
    while True:
        vis_lager()
        valgt_vare = input("Indtast varenavn (eller 'stop' for at afslutte): ")
        if valgt_vare == 'stop':
            break
        
        if valgt_vare in varer:
            index = varer.index(valgt_vare)
            køb = int(input("Hvor mange vil du købe? "))
            if køb <= lager[index]:
                lager[index] -= køb
                print("Du har købt", køb)
            else:
                print("Ikke nok på lager.")
        else:
            print("Ugyldigt valg. Prøv igen.")

def genopfyldning():
    while True:
        vis_lager()
        valgt_vare = input("Indtast varenavn for genopfyldning (eller 'stop' for at afslutte): ")
        if valgt_vare == 'stop':
            break
        
        if valgt_vare in varer:
            index = varer.index(valgt_vare)
            køb = int(input("Hvor mange vil du tilføje? "))
            lager[index] += køb
        elif valgt_vare == "alle":
            køb = int(input("Hvor mange vil du tilføje til alle? "))
            for i in range(len(lager)):
                lager[i] += køb
        else:
            print("Ugyldigt valg. Prøv igen.")

def main():
    while True:
        valg = input("\nVælg handling (1: Salg, 2: Genopfyld, 3: Vis lager, 4: Afslut): ")
        if valg == '1':
            salg()
        elif valg == '2':
            genopfyldning()
        elif valg == '3':
            vis_lager()
        elif valg == '4':
            print("Afslutter programmet.")
            vis_lager()
            break
        else:
            print("Ugyldigt valg. Prøv igen.")

if __name__ == "__main__":
    main()
