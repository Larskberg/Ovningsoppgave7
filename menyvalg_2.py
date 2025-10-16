# Legg til nytt emne ved bruk av studieplan.py, sjekk om gyldighet skjer via studieplan.py
from studieplan import legg_til_emne


def legg_til_nytt_emne():
    print("\n--- Legg til emne i studieplan ---")
    emne_index = int(input("Indeks på emne: "))
    sem_nr = int(input("Semester (1-6): "))
    legg_til_emne(emne_index, sem_nr)
