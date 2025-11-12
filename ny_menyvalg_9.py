# Lagrer studieplan til en txt fil
#from emner import emnekoder, semestre, studiepoeng
#from studieplan import hent_studieplan

from ny_emner import emner_dict, studieplan_dict, Emner, Studieplan


def studieplanfil():
    try:
        filnavn = 'studieplan.txt'
        
        with open(filnavn, "w") as fila:
            for i in studieplan_dict:
                fila.write(f"{studieplan_dict[i]}")
                for sem_nr, sem in enumerate(studieplan_dict[i].emner):
                    fila.write(f'{sem_nr}. semester:\n')
                    for j in sem:
                        fila.write(
                            f"{studieplan_dict[i].emner[j]}\n"
                    )
        print("Laget fil med studieplan")
    except TypeError:
        print('Kan ikkke lage studieplanfil')





def emnefil():
    try:
        filnavn = 'emner.txt'
        with open(filnavn, 'w') as fila:
            for i in emner_dict:
                fila.write(f'{emner_dict[i]}\n')
        print("Laget fil med emner")
    except TypeError:
        print('Kan ikke lage emnefil')

