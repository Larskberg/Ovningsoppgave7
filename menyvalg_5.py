# Sjekk studieplan for gyldighet
from studieplan import hent_studieplan
from emner import studiepoeng

def gyldig_semestre():
    studieplan = hent_studieplan()
    ugyldig = []

    for i, sem in enumerate(studieplan):
        poeng = sum(studiepoeng[j] for j in sem)
        if poeng != 30:
            ugyldig.append((i + 1, poeng))

    if not ugyldig:
        print("Studieplanen er gyldig")
    else:
        print("Studieplanen er ikke gyldig")
        for sem, poeng in ugyldig:
            print(f"Semester {sem} har {poeng} poeng")