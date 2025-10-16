# Printer ut registrerte emner og indekser
from emner import emnekoder, semestre, studiepoeng


def print_ut_emner():
    print("\nRegistrerte emner:")
    if not emnekoder:
        print("Ingen emner registrert ennå.")
    for i, kode in enumerate(emnekoder):
        print(f"{i}: {kode} ({semestre[i]}, {studiepoeng[i]} sp)")
