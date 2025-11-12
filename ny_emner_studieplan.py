emner_dict = {}
studieplan_dict = {}

class Emner:
    
    def __init__(self, emnekode, navn, semester, studiepoeng):
        self.emnekode = emnekode
        self.navn = navn
        self.studiepoeng = studiepoeng
        self.semester = semester
        
    def __str__(self):
        return f'Emnekode: {self.emnekode} Navn: {self.navn} Semester: {self.semester} Studiepoeng: {self.studiepoeng}'
        
        
        
        
        
        
class Studideplan:
    
    def __init__(self, ID, tittel):
        self.ID = ID
        self.tittel = tittel
        self.emner = [[] for _ in range(6)]
        
    def __str__(self):
        return f'ID: {self.ID} Tittel: {self.tittel}'
    
    
        
    def legg_til_emne(self, emne):
        self.emner.append(emne)
        
#mneyvalg 6, skriv ut en studieplan
    def skriv_ut(self):
        print(f'{ID}\n)
        for sem, liste in self.emner:
            
        
        
        print("\nStudieplan:")
        for i, sem in enumerate(hent_studieplan(), start=1):
            total_sp = sum(studiepoeng[j] for j in sem)
            emner = [emnekoder[j] for j in sem]
            print(f"Semester {i}: {emner} ({total_sp} sp)")
        
#menyvagl 7      
    def gyldig_semestre(self):

        ugyldig = []

        for i, sem in enumerate(self.emner):
            poeng = sum(self.emner[j].studiepoeng for j in sem)
            if poeng != 30:
                ugyldig.append((i + 1, poeng))

        if not ugyldig:
            print("Studieplanen er gyldig")
        else:
            print("Studieplanen er ikke gyldig")
            for sem, poeng in ugyldig:
                print(f"Semester {sem} har {poeng} poeng")
                
#finn hvilke studieplaner som bruker et oppgitt emne. menyvalg 8

    def sjekk_studieplan(self):
        sjekk = input('Hvilket emne vil du sjekke?')
        if sjekk not in emner_dict:
            print('Emne er ikke registrert')
            
        else:
            for i in studieplan_dict:
                if sjekk in studieplan_dict[i].emner:
                    print(studieplan_dict[i])

    

