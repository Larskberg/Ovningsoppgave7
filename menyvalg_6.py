# Lagrer studieplan til en txt fil
from emner import emnekoder, semestre, studiepoeng
from studieplan import hent_studieplan


def studieplanfil():
    try:
        filnavn = 'studieplan.txt'
        studieplan = hent_studieplan()
        with open(filnavn, "w") as fila:
            for sem_nr, sem in enumerate(studieplan, start=1):
                fila.write(f"{sem_nr}. semester:\n")
                for i in sem:
                    fila.write(
                        f"{emnekoder[i]}, {studiepoeng[i]}, {semestre[i]}\n"
                    )
        print("Laget fil med studieplan")
    except TypeError:
        print('Kan ikkke lage studieplanfil')

def emnefil():
    try:
        filnavn = 'emner.txt'
        with open(filnavn, 'w') as fila:
            for i, kode in enumerate(emnekoder):
                fila.write(f"{kode}, {studiepoeng[i]}, {semestre[i]}\n")
        print("Laget fil med emner")
    except TypeError:
        print('Kan ikke lage emnefil')

