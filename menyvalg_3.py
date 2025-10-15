from emner import emnekoder, semestre, studiepoeng

def kjør3():
    print("\nRegistrerte emner:")
    if not emnekoder:
        print("Ingen emner registrert ennå.")
    for i, kode in enumerate(emnekoder):
        print(f"{i}: {kode} ({semestre[i]}, {studiepoeng[i]} sp)")
