#menyvalg 7   
from emner import emner
from menyvalg_5 import studieplaner, Studieplan


def gyldig_semestre():
#liste for ugyldige semestre
    ugyldig = []
    
    print("\n--- Gyldighetsjekk ---")

    # Sjekk om det finnes noen studieplaner
    if not studieplaner:
        print("Ingen studieplaner finnes. Lag en ny først.")
        return

    # Vis tilgjengelige studieplaner
    print("Tilgjengelige studieplaner:")
    for i, plan in enumerate(studieplaner.keys(), start=1):
        print(f"{i}. {plan}")

    # Sjekker gyldig studieplan index
    try:
        plan_valg = int(input("Velg studieplan (nummer): "))
        if plan_valg < 1 or plan_valg > len(studieplaner):
            print("Ugyldig valg.")
            return
        valgt_plan = list(studieplaner.keys())[plan_valg - 1]
    except ValueError:
        print("Ugyldig input. Må være et tall.")
        return

    # Sjekker at det er 30 sp i hvert semester
    # Hvis det ikke er det, legger til i ugyldig liste og skriver ut
    for sem, emneliste in studieplaner[valgt_plan].semestre.items():
        if emneliste:
            poeng = sum(emne.studiepoeng for emne in emneliste)
            if poeng != 30:
                ugyldig.append((sem, poeng))
        else:
            ugyldig.append((sem, 0))

    if not ugyldig:
        print("Studieplanen er gyldig")
    else:
        print("Studieplanen er ikke gyldig")
        for sem, poeng in ugyldig:

            print(f"Semester {sem} har {poeng} poeng")
