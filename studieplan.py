# Studieplanen som brukes i menyvalg 2, 4 og 5. Sjekker over alle regler for å legge til emner.
from emner import emnekoder, semestre, studiepoeng

studieplan = [[] for _ in range(6)]

def legg_til_emne(emne_index, semester_nr):
    if emne_index < 0 or emne_index >= len(emnekoder):
        print("Ugyldig emneindeks.")
        return
    
    for sem in studieplan:
        if emne_index in sem:
            print("Emnet er allerede lagt til i studieplanen.")
            return
    
    sem_type = semestre[emne_index]
    if sem_type == "høst" and semester_nr not in [1,3,5]:
        print("Dette emnet kan bare legges til i høstsemester (1,3,5).")
        return
    if sem_type == "vår" and semester_nr not in [2,4,6]:
        print("Dette emnet kan bare legges til i vårsemester (2,4,6).")
        return
    
    total_sp = sum(studiepoeng[i] for i in studieplan[semester_nr-1])
    if total_sp + studiepoeng[emne_index] > 30:
        print("Semesteret har ikke plass til flere studiepoeng.")
        return
    
    studieplan[semester_nr-1].append(emne_index)
    print(f"Emnet {emnekoder[emne_index]} lagt til i semester {semester_nr}.")

def hent_studieplan():
    return studieplan
