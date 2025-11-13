#menyvalg 6, skriv ut en studieplan
  

from emner import emner
from menyvalg_5 import studieplaner, Studieplan

def skriv_ut_studieplan():
    print("\n--- Skriv ut studieplan ---")

    # Sjekk om det finnes noen studieplaner
    if not studieplaner:
        print("Ingen studieplaner finnes. Lag en ny først.")
        return

    # Vis tilgjengelige studieplaner
    print("Tilgjengelige studieplaner:")
    for i, plan in enumerate(studieplaner.keys(), start=1):
        print(f"{i}. {plan}")

    try:
        plan_valg = int(input("Velg studieplan (nummer): "))
        if plan_valg < 1 or plan_valg > len(studieplaner):
            print("Ugyldig valg.")
            return
        valgt_plan = list(studieplaner.keys())[plan_valg - 1]
    except ValueError:
        print("Ugyldig input. Må være et tall.")
        return

    # Sjekk om det finnes emner i valgt plan
    if not studieplaner[valgt_plan]:
        print(f"Studieplan '{valgt_plan}' har ingen emner.")
        return

    # Vis emner i valgt plan
    print(f"Studieplan '{valgt_plan}':")
    
    for sem, Emner in studieplaner[valgt_plan].semestre.items():
        print(f'{sem}. semester:\n')
        if emner:
            for emne in Emner:
                print(f" - {emne}")
        else: 
            print(' Ingen emner')
