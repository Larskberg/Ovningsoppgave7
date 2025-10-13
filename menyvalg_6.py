#lag en fil av studieplanen

def studieplan(emnekode, studiepoeng, semester):
    filnavn = 'studieplan.txt'
    with open(filnavn, "w") as fila:
        for emne in emne_liste:
            #skrive fil med 3 verdier per inje
            fila.write('\n' + emnekode, studiepoeng, semester)
            
            print('Laget fil med studieplan')
           