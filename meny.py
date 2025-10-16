# Hovedmeny
from menyvalg_1 import lag_nytt_emne
from menyvalg_2 import legg_til_nytt_emne
from menyvalg_3 import print_ut_emner
from menyvalg_4 import print_studieplan
from menyvalg_5 import gyldig_semestre
from menyvalg_6 import studieplanfil, emnefil
from menyvalg_7 import les_fra_fil


def meny():
    while True:
        print("\n--- Studieplan meny ---")
        print("1. Legg til nytt emne")
        print("2. Legg til emne i studieplan")
        print("3. Skriv ut alle emner")
        print("4. Skriv ut studieplan")
        print("5. Sjekk gyldighet")
        print("6. Lagre til fil")
        print("7. Les fra fil")
        print("8. Avslutt")

        valg = input("Velg: ")

        if valg == "1":
            lag_nytt_emne()
        elif valg == "2":
            legg_til_nytt_emne()
        elif valg == "3":
            print_ut_emner()
        elif valg == "4":
            print_studieplan()
        elif valg == "5":
            gyldig_semestre()
        elif valg == "6":
            studieplanfil()
            emnefil()
        elif valg == "7":
            les_fra_fil()
        elif valg == "8":
            print("Avslutter...")
            break
        else:
            print("Ugyldig valg.")


if __name__ == "__main__":
    meny()
