try: 
    x = int(input("indtast et tal"))
    print (10/x)
except ValueError:
    print("det var ikke et gyldigt tal")
except ZeroDivisionError:
    print("kan ikke dividere med 0. ")