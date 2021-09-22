# Agora iremos usar as condições if,elif e else

A = 200
b = 300

if A > b: # Condição if
    print('A é maior que b')
    print(f'{A} é maior que {b}') # ultizando variáveis no print

elif A == b:
    '''Condição elif, onde o compilador fará outra comparação caso
       não entre no primeiro if'''
    print('A é igual a b')


else:   #Condição else, ocorrerá caso nenhuma das condições anteriores sejam satisfeitas
    print('A é menor que b')
