# Hovedmeny
from menyvalg_1 import lag_nytt_emne
from menyvalg_2 import legg_til_nytt_emne
from menyvalg_3 import fjern_emne_fra_studieplan
from menyvalg_4 import print_ut_emner
from menyvalg_5 import lag_ny_studieplan
from menyvalg_6 import skriv_ut_studieplan
from menyvalg_7 import gyldig_semestre
from menyvalg_8 import finn_studieplaner_med_emne
from menyvalg_9 import lagre_til_fil
from menyvalg_10 import les_fra_fil


def meny():
    while True:
        print("\n--- Hovedmeny ---")
        print("1. Legg til nytt emne")
        print("2. Legg til emne i studieplan")
        print("3. Fjern emne fra studieplan")
        print("4. Skriv ut liste av alle registrerte emner")
        print("5. Lag en ny tom studieplan")
        print("6. Skriv ut en studieplan med hvilke emner som er i hvert semester")
        print("7. Finn hvilke studieplaner er gyldig eller ikke")
        print("8. Finn hvilke studieplaner som inneholder et emne")
        print("9. Lagre emner og studieplaner til fil")
        print("10. Les inn emner og studieplaner fra fil")
        print("11. Avslutt")

        valg = input("Velg: ")

        if valg == "1":
            lag_nytt_emne()
        elif valg == "2":
            legg_til_nytt_emne()
        elif valg == "3":
            fjern_emne_fra_studieplan()
        elif valg == "4":
            print_ut_emner()
        elif valg == "5":
            lag_ny_studieplan()
        elif valg == "6":
            skriv_ut_studieplan()
        elif valg == "7":
            gyldig_semestre()
        elif valg == "8":
            finn_studieplaner_med_emne()
        elif valg == "9":
            lagre_til_fil()
        elif valg == "10":
            les_fra_fil()
        elif valg == "11":
            print("Avslutter...")
            break
        else:
            print("Ugyldig valg.")


if __name__ == "__main__":
    meny()
