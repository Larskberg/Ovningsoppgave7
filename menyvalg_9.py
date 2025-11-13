#menyvalg_9 lagre til fil
from emner import emner
from menyvalg_5 import studieplaner, Studieplan

def lagre_til_fil():
    
        try:
            filnavn = 'studieplan.txt'
            #lager fil og skriver:
            with open(filnavn, "w") as fila:
                #for hver studieplan:
                for key in studieplaner:
                    fila.write(f"\n{studieplaner[key].plan_id}\n {studieplaner[key].tittel}\n")
                    for sem, Emner in studieplaner[key].semestre.items():
                        fila.write(f'\n{sem}. semester:\n')
                        if emner:
                            for emne in Emner:
                                fila.write(f" - {emne}")
                        else: 
                            fila.write(' Ingen emner')
            print("Laget fil med studieplan")
        except TypeError:
            print('Kan ikkke lage studieplanfil')






        try:
            filnavn = 'emner.txt'
            with open(filnavn, 'w') as fila:
                for i, e in enumerate(emner, start=1):
                    fila.write(f'{i}: {e}\n')
            print("Laget fil med emner")
        except TypeError:
            print('Kan ikke lage emnefil')


