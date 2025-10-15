#les opp emnene i fil fra menyvalg 6

with open('studieplan.txt', 'r') as fila:
    print('Studieplan:')
    for linje in fila:
        print(linje + '\n')
        
        
        
with open('emner.txt', 'r') as fila:
    print('Emner:')
    for linje in fila:
        print(linje + '\n')
        

        