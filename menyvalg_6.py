#lag en fil av studieplanen
from emner import emnekoder, semestre, studiepoeng
from studieplan import hent_studieplan

studieplan = hent_studieplan()

def studieplanfil():
    try:
        filnavn = 'studieplan.txt'
        with open(filnavn, "w") as fila:
            for liste in studieplan:
                semester_linje = f'{liste + 1}. semster:\n'
                fila.write(semester_linje)
                for i, liste in studieplan:
                    linje = f'{emnekoder[i]}, {studiepoeng[i]}, {semestre[i]}\n'
                    
                    fila.write(linje)
                
            print('Laget fil med studieplan')
    except TypeError:
       print('Kan ikke lage fil med studieplan')
   
        
def emnefil():
    try:
        filnavn = 'emner.txt'
        with open(filnavn, 'w') as fila:
            for i in emnekoder:
                linje = f'{emnekoder[i]}, {studiepoeng[i]}, {semestre[i]}\n'
                fila.write(linje)
                
            print('Laget fil med emner')
    except TypeError:
        print('Kan ikke lage fil med emnekoder')