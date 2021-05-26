adulti = []
minori = []

with open("date_intrare") as f:
    for s in f:
        i = s.index(" ")
        nume = s[0:i]
        varsta = int(s[i+1:-1])

        if varsta >= 18:
            adulti.append(nume)
        else:
            minori.append(nume)

fisier = "Adulti.txt", "Minori.txt"
text = "Adulti", "Minori"
lista= adulti, minori

def salvare(fisier, text, lista):
    with open(fisier, "w") as f:
        f.write(f"{text} \n")
        f.write("-" * 10)
        f.write("\n")
        for i in lista:
            f.write(f"{i} \n")

optiune = input("Alege varianta a sau b ")
if optiune == "a":
    print("Adulti", "\n", "-" * 10)
    for adult in adulti:
        print(adult)
    print("Minori", "\n", "-" * 10)
    for minor in minori:
        print(minor)
elif optiune == "b":
        salvare("Adulti.txt","Adulti",adulti)
        salvare("Minori.txt", "Minori", minori)
else:
    while optiune not in ["a", "b"]:
        print("Varianta incorecta")
        optiune = input("Alege varianta a sau b ")



