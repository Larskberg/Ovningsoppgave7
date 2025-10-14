emnekoder = []
semestre = []   # "høst" eller "vår"
studiepoeng = []

def nytt_emne(kode, semester, sp):
    emnekoder.append(kode)
    semestre.append(semester.lower())
    studiepoeng.append(sp)

def skriv_ut_emner():
    print("\nRegistrerte emner:")
    for i, kode in enumerate(emnekoder):
        print(f"{i}: {kode} ({semestre[i]}, {studiepoeng[i]} sp)")