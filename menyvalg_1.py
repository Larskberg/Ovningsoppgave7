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

        # Valider studiepoeng
        sp = int(input("Studiepoeng: "))

        # Sjekk konsistens: samme emne kan ikke ha både H og V
        for e in emner:
            if e.kode == kode and e.semester != sem:
                print(f"Feil: Emnet {kode} er allerede registrert med semester {e.semester}.")
                return

        nytt_emne = Emne(kode, sem, sp)
        emner.append(nytt_emne)

        print(f"Emnet {nytt_emne} er registrert.")

    except ValueError:
        print("Ugyldig input. Studiepoeng må være et tall.")
