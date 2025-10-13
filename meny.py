# Menyvalg
import menyvalg_1
import menyvalg_2
import menyvalg_3
import menyvalg_4
import menyvalg_5
import menyvalg_6
import menyvalg_7

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
            kode = input("Emnekode: ")
            sem = input("Semester (høst/vår): ")
            sp = int(input("Studiepoeng: "))
            menyvalg_1(kode, sem, sp)
        elif valg == "2":
            emne_index = int(input("Indeks på emne: "))
            sem_nr = int(input("Semester (1-6): "))
            menyvalg_2(emne_index, sem_nr)
        elif valg == "3":
            menyvalg_3()
        elif valg == "4":
            menyvalg_4()
        elif valg == "5":
            menyvalg_5()
        elif valg == "6":
            menyvalg_6()
        elif valg == "7":
            menyvalg_7()
        elif valg == "8":
            print("Avslutter...")
            break
        else:
            print("Ugyldig valg.")

if __name__ == "__main__":
    meny()