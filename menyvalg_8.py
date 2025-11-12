#finn hvilke studieplaner som bruker et oppgitt emne. menyvalg 8
from emner import emner
from menyvalg_5 import studieplaner, Studieplan

def finn_studieplaner_med_emne():
    sjekk = input('Hvilket emne vil du sjekke?')
    if sjekk not in emner:
        print('Emne er ikke registrert')
        
    else:
        for key in studieplaner:
             if any(sjekk in emneliste for emneliste in sjekk.semestre.values()):
                 print(studieplaner[key])
