#finn hvilke studieplaner som bruker et oppgitt emne. menyvalg 8
from emner import emner
from menyvalg_5 import studieplaner, Studieplan

def finn_studieplaner_med_emne():
    print('Emner:')
    for emne in emner:
        print(f' - {emne}')
    sjekk = input('Hvilket emne vil du sjekke?')
    if sjekk in emner[1]:
        
        for key in studieplaner:
            if any(sjekk in emneliste for emneliste in key.semestre.values()):
                     print(studieplaner[key])
            else:
                print('Emne finnes ikke i noen studieplan')
                    
    if sjekk not in emner:
        print('Emne er ikke registrert')
        
   
