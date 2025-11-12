# Printer ut registrerte emner og indekser
#from emner import emnekoder, semestre, studiepoeng
from ny_emner import emner_dict, Emner

def print_ut_emner():
    print("\nRegistrerte emner:")
    if not emner_dict:
        print("Ingen emner registrert ennå.")
    for i in emner_dict:
        print(emner_dict[i])
