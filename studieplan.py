# Studieplanen, sjekker gjennom alle krav før man kan legge et emne inn i studieplanen
from emner import emnekoder, semestre, studiepoeng

studieplan = [[] for _ in range(6)]

def legg_til_emne(emne_index, semester_nr):
    # Sjekk at indeksen er gyldig
    if emne_index < 0 or emne_index >= len(emnekoder):
        print("Ugyldig emneindeks.")
        return
    
    # Hent emnekoden vi prøver å legge til
    kode = emnekoder[emne_index]

    # Sjekk om emnet allerede finnes i planen (uavhengig av semester)
    for sem in studieplan:
        if any(emnekoder[i] == kode for i in sem):
            print(f"Emnet {kode} er allerede lagt til i studieplanen.")
            return

    # Sjekk semester-type (høst/vår)
    sem_type = semestre[emne_index]
    if sem_type == "høst" and semester_nr not in [1, 3, 5]:
        print("Dette emnet kan bare legges til i høstsemester (1,3,5).")
        return
    if sem_type == "vår" and semester_nr not in [2, 4, 6]:
        print("Dette emnet kan bare legges til i vårsemester (2,4,6).")
        return

    # Sjekk at semesteret ikke overstiger 30 studiepoeng
    total_sp = sum(studiepoeng[i] for i in studieplan[semester_nr-1])
    if total_sp + studiepoeng[emne_index] > 30:
        print("Semesteret har ikke plass til flere studiepoeng.")
        return

    # Legg til emnet
    studieplan[semester_nr-1].append(emne_index)
    print(f"Emnet {kode} lagt til i semester {semester_nr}.")

def hent_studieplan():
    return studieplan
