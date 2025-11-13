from emner import Emne, emner

def lag_nytt_emne():
    try:
        print("\n--- Legg til nytt emne ---")
        kode = input("Emnekode: ")

        # Valider semester
        while True:
            sem_input = input("Semester (høst/vår): ").lower()
            if sem_input == "høst":
                sem = "H"
                break
            elif sem_input == "vår":
                sem = "V"
                break
            else:
                print("Ugyldig valg. Du må skrive 'høst' eller 'vår'.")

        sp = int(input("Studiepoeng: "))

        for e in emner:
            # Hindre nøyaktig duplikat (samme kode og semester)
            if e.kode == kode and e.semester == sem:
                print(f"Feil: Emnet {kode} er allerede registrert for semester {e.semester}.")
                return
            # Samme emne kan ikke ha forskjellige semestre
            if e.kode == kode and e.semester != sem:
                print(f"Feil: Emnet {kode} er allerede registrert med semester {e.semester}.")
                return

        nytt_emne = Emne(kode, sem, sp)
        emner.append(nytt_emne)

        print(f"Emnet {nytt_emne} er registrert.")

    except ValueError:
        print("Ugyldig input. Studiepoeng må være et tall.")
