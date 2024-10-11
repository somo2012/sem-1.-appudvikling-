import random 
valg = 0 
while (valg) != 1:
    valg = random.randint (1,2)
    print (f"valgt: {valg}")
print("løkken stoppede, fordi der blev valgt 1")

while True: 
    svar= input("skriv 'stop' for at afslutte: ")
    if svar =="stop":
        break

