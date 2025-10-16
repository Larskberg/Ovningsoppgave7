# Lag nytt emne
from emner import emnekoder, semestre, studiepoeng


def lag_nytt_emne():
    try:
        print("\n--- Legg til nytt emne ---")
        kode = input("Emnekode: ")

        # Valider semester
        while True:
            sem = input("Semester (høst/vår): ").lower()
            if sem in ("høst", "vår"):
                break
            else:
                print("Ugyldig valg. Du må skrive 'høst' eller 'vår'.")

        # Valider studiepoeng
        sp = int(input("Studiepoeng: "))

        emnekoder.append(kode)
        semestre.append(sem)
        studiepoeng.append(sp)
        print(f"Emnet {kode} ({sem}, {sp} sp) er registrert.")

    except ValueError:
        print("Ugyldig input. Studiepoeng må være et tall.")
        
