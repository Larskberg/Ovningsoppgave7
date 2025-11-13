from emner import Emne, emner
from menyvalg_5 import studieplaner

def legg_til_nytt_emne():
    print("\n--- Legg til emne i studieplan ---")

    # Sjekk om det finnes registrerte emner
    if not emner:
        print("Ingen emner registrert. Bruk menyvalg 1.")
        return

    # Sjekk om det finnes studieplaner
    if not studieplaner:
        print("Ingen studieplaner finnes. Bruk menyvalg 5.")
        return

    # Velg emne
    print("Tilgjengelige emner:")
    for i, e in enumerate(emner, start=1):
        print(f"{i}. {e}")

    try:
        valg = int(input("Velg emne (nummer): "))
        if valg < 1 or valg > len(emner):
            print("Ugyldig valg.")
            return
        valgt_emne = emner[valg - 1]
    except ValueError:
        print("Ugyldig input. Må være et tall.")
        return

    # Velg studieplan
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

    # Velg semester
    print("Tilgjengelige semestre:")
    for sem in studieplaner[valgt_plan].semestre.keys():
        print(f" - Semester {sem}")
    
    try:
        valgt_semester = int(input("Velg semester (nummer 1-6): "))
        if valgt_semester < 1 or valgt_semester > 6:
            print("Ugyldig semester.")
            return
    except ValueError:
        print("Ugyldig input. Må være et tall.")
        return

    # Sjekker konsistens
    for e in studieplaner[valgt_plan].semestre[valgt_semester]:
        if e.kode == valgt_emne.kode:
            print(f"Feil: Emnet {valgt_emne.kode} finnes allerede i semester {valgt_semester}.")
            return

    # Legg til emnet i valgt semester
    studieplaner[valgt_plan].semestre[valgt_semester].append(valgt_emne)
    print(f"Emnet {valgt_emne} er lagt til i studieplan '{valgt_plan}', semester {valgt_semester}.")
