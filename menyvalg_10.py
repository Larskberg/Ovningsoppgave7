# Leser opp emner fra txt fil lagret fra menyvalg 9
def les_fra_fil():
    with open('studieplan.txt', 'r') as fila:
        print('Studieplan:')
        for linje in fila:
            print(linje + '\n')
            
            
            
    with open('emner.txt', 'r') as fila:
        print('Emner:')
        for linje in fila:
            print(linje + '\n')

    