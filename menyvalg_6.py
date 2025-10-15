#lag en fil av studieplanen
from emner import emnekoder, semestre, studiepoeng
from studieplan import studieplan

def studieplanfil(studieplan):
    filnavn = 'studieplan.txt'
    with open(filnavn, "w") as fila:
        for liste in studieplan:
            semester_linje = f'{liste}. semster:\n'
            fila.write(semester_linje)
            for i, liste in studieplan:
                linje = f'{emnekoder[i]}, {studiepoeng[i]}, {semestre[i]}\n'
                
                fila.write(linje)
            
        print('Laget fil med studieplan')
           
def emnefil(emnekoder):
    filnavn = 'emner.txt'
    with open(filnavn, 'w') as fila:
        for i in emnekoder:
            linje = f'{emnekoder[i]}, {studiepoeng[i]}, {semestre[i]}\n'
            fila.write(linje)
            
        print('Laget fil med emner')