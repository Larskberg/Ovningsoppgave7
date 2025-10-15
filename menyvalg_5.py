#sjekke om stuideplanen har 6 semestre med 30 studiepoeng
#skriv ut evt semestre som ikke er gyldig 
#og hvor mange studiepoeng det er i det semesteret



from studieplan import hent_studieplan
from emner import studiepoeng

studieplan = hent_studieplan()

def gyldig_semestre():
    poeng = 0
    ugyldig = []
    for i, sem in enumerate(hent_studieplan(), start=1):
        poeng = sum(studiepoeng[j] for j in sem)
        
        if poeng != 30:
            ugyldig.append([i + 1, poeng])
            
    if not ugyldig:
        print('Studieplanen er gyldig')
    
    else:
        print('studieplanen er ikke gyldig')
    for i, poeng in enumerate(ugyldig):
        print(f'Semester {i} har {poeng} poeng')
        
        


#gjøre om emne_index til studiepoeng

#sjekke for hvert semester at det er 30poeng
#hvis det ikke er 30poeng, skriv ut hvilket semester og hvor mange poeng