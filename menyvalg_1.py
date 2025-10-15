# Lager et nytt emne
from emner import emnekoder, semestre, studiepoeng

def kjør1():
    print("\n--- Legg til nytt emne ---")
    kode = input("Emnekode: ")
    sem = input("Semester (høst/vår): ").lower()
    sp = int(input("Studiepoeng: "))
    emnekoder.append(kode)
    semestre.append(sem)
    studiepoeng.append(sp)

    print(f"Emnet {kode} ({sem}, {sp} sp) er registrert.")
