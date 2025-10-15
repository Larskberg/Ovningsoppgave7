# hovedmeny.py
from menyvalg_1 import kjør1
from menyvalg_2 import kjør2
from menyvalg_3 import kjør3
from menyvalg_4 import kjør4
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
            kjør1()
        elif valg == "2":
            kjør2()
        elif valg == "3":
            kjør3()
        elif valg == "4":
            kjør4()
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