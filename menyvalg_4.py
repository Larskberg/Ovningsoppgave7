from emner import emnekoder, studiepoeng
from studieplan import hent_studieplan

def kjør4():
    print("\nStudieplan:")
    for i, sem in enumerate(hent_studieplan(), start=1):
        total_sp = sum(studiepoeng[j] for j in sem)
        emner = [emnekoder[j] for j in sem]
        print(f"Semester {i}: {emner} ({total_sp} sp)")
