#finn hvilke studieplaner som bruker et oppgitt emne. menyvalg 8
from emner import emner
from menyvalg_5 import studieplaner, Studieplan

def finn_studieplaner_med_emne():
    print('\n--- Finn studieplan med emne ---')
    print('Emner:')
    for emne in emner:
        print(f' - {emne}')
    sjekk = input('Hvilket emne vil du sjekke? ')

    # Sjekk om emne finnes
    emne_finnes = any(e.kode == sjekk for e in emner)
    if not emne_finnes:
        print('Emne er ikke registrert')
        return
#liste med planer som har gitt emne i seg
    planer_med_emne = []
    for plan in studieplaner.values():
        funnet = False
        for emneliste in plan.semestre.values():
            for e in emneliste:
                if e.kode == sjekk:
                    planer_med_emne.append(plan.tittel)
                    funnet = True
                    break
            if funnet:
                break
#hvis noen planer har emnet, så ligger planene i lista og blir skrevet ut
    if planer_med_emne:
        print(f'\nStudieplaner som inneholder emne {sjekk}:')
        for plan_tittel in planer_med_emne:
            print(f' - {plan_tittel}')
    else:
        print(f'Emne {sjekk} finnes ikke i noen studieplan')

