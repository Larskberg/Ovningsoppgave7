# Emneliste
emnekoder = []
semestertyper = []  # Bruker skriver inn høst eller vår
studiepoeng = []

# Studieplan: 6 semestre
studieplan = [[] for _ in range(6)]

def lag_emne():
    kode = input("Skriv emnekode: ")
    semester = input("Undervises i (høst/vår): ").lower()
    if semester not in ["høst", "vår"]:
        print("Ugyldig semester, må være 'høst' eller 'vår'.")
        return
    sp = int(input("Antall studiepoeng: "))

    emnekoder.append(kode)
    semestertyper.append(semester)
    studiepoeng.append(sp)
    print(f"Emne {kode} lagt til.")

