# Loop For
print('-'*12, 'For', '-'*12)
for i in range(5):  # Loop usado em conjunto com a função range
    print(i) # enquanto i estiver dentro de um range menor 5, será printado seu valor

# também pode-se escolher de onde deve-se começar a contagem do seu range
print('-'*30)
for i in range(1, 5):
    print(i)

# Por fim, pode-se escolher como será feita essa contagem.(Ex: pulando de 2 em 2)
print('-'*30)
for i in range(0, 5, 2):
    print(i)

# While
print('-'*11, 'While', '-'*12)
cont = 0
while cont <= 5:    #Loop usado em conjunto com uma condição que se deseja
    print(cont)
    cont += 1

print('-'*9, 'While True', '-'*9)
cont = 0
while True:
    '''Loop infinito, o mesmo é usado para se fazer um número de interações em que o usuário
    não sabe a quantidade de vezes que precisará rodar o programa'''
    print(cont)
    if cont >= 5:
        break   # Condição de parada do Loop infinito
    cont += 1
