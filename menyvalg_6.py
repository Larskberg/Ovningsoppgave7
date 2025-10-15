# menyvalg_6.py
from emner import emnekoder, semestre, studiepoeng
from studieplan import hent_studieplan

def studieplanfil():
    filnavn = 'studieplan.txt'
    studieplan = hent_studieplan()
    with open(filnavn, "w") as fila:
        for sem_nr, sem in enumerate(studieplan, start=1):
            fila.write(f"{sem_nr}. semester:\n")
            for i in sem:
                fila.write(f"{emnekoder[i]}, {studiepoeng[i]}, {semestre[i]}\n")
    print("Laget fil med studieplan")

def emnefil():
    filnavn = 'emner.txt'
    with open(filnavn, 'w') as fila:
        for i, kode in enumerate(emnekoder):
            fila.write(f"{kode}, {studiepoeng[i]}, {semestre[i]}\n")
    print("Laget fil med emner")