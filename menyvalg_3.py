from emner import emner
from menyvalg_5 import studieplaner

def fjern_emne_fra_studieplan():
    print("\n--- Fjern emne fra studieplan ---")

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
    print(f"Emner i studieplan '{valgt_plan}':")
    for i, e in enumerate(studieplaner[valgt_plan], start=1):
        print(f"{i}. {e}")

    try:
        emne_valg = int(input("Velg emne som skal fjernes (nummer): "))
        if emne_valg < 1 or emne_valg > len(studieplaner[valgt_plan]):
            print("Ugyldig valg.")
            return
        fjernet_emne = studieplaner[valgt_plan].pop(emne_valg - 1)
        print(f"Emnet {fjernet_emne} er fjernet fra studieplan '{valgt_plan}'.")
    except ValueError:
        print("Ugyldig input. Må være et tall.")
