#fjern et emne
from ny_emner import emner_dict

def fjern_emne():
    while True:
        fjern = input('Hvilket emne vil du fjerne? Skriv emnekode: ')
        if fjern not in emner_dict:
            print(f'{fjern} finnes ikke.')
        else:
            emner_dict.pop(fjern)
            break