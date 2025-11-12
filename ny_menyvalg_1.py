# Lag nytt emne
#from emner import emnekoder, semestre, studiepoeng
from ny_emner import Emner, emner_dict

#def lag_nytt_emne():
#    print("\n--- Legg til nytt emne ---")
 #   kode = input("Emnekode: ")
  #  sem = input("Semester (høst/vår): ").lower()
   # sp = int(input("Studiepoeng: "))
    #emnekoder.append(kode)
    #semestre.append(sem)
    #studiepoeng.append(sp)
    #print(f"Emnet {kode} ({sem}, {sp} sp) er registrert.")


def lag_nytt_emne():
    print("\n--- Legg til nytt emne ---")
    kode = input("Emnekode: ")
    navn = input("Emnenavn: ")
    sem = input("Semester (høst/vår): ").lower()
    sp = int(input("Studiepoeng: "))
    emne = Emner(kode, navn, sem, sp)
    emner_dict[kode] = emne
    print(f"Emnet {kode} ({sem}, {sp} sp) er registrert.")