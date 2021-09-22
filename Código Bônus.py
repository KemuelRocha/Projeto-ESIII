Jogador = dict()  # criação de um dicionário
Todos = list()    # criação de uma lista
Gols = list()     # criação de uma lista

while True:         # Loop infinito
    Jogador.clear()  # Limpa tudo que está dentro do dicionário Jogador

    Jogador['Nome'] = str(input('Nome do Jogador: ')).strip()   # Adiciona à chave Nome do dicionário Jogador, um valor que o usuário fornece
    # Função strip é usada para retirar espaços tanto do inicio tanto do fim.

    part = int(input(f'Quantas partidas {Jogador["Nome"]} Jogou? ')) # A variavél part recebe um valor inteiro fornecido pelo usuário

    for c in range(part): # Loop for com um tamanho de part, que foi fornecido pelo usuário
        Gols.append(int(input(f' Quantos Gols na partida {c+1}? ')))    # Adiciona na lista Gols um valor fornecido pelo usuário
    Jogador['Gols'] = Gols[:]   # Faz uma cópia da lista Gols para o dicionário com a chave Gols

    Jogador['Total'] = sum(Gols)    # Adiciona na chave do dicionário Jogador Total o somatório da lista gols

    Todos.append(Jogador.copy())    # A lsita Todos recebe uma copia de todo dicionário Jogador

    Gols.clear() # Limpa a lista Gols
    while True:
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opção in 'SN':   # Condição if que verifica se S ou N está dentro da variavel opção
            break
        else:
            print('ERRO! Digite Somente S ou N')
    if opção == 'N':    # Condição de parada para o cadastramento de jogadores
        break

print('-='*30)
print('-'*40)
print('cod ', end='')
for i in Jogador.keys():    # loop nas chaves do dicionário
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(Todos):   # Loop com enumeração dos valores que estão dentro da lista Todos
    print(f'{k+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)')) - 1
    if busca == 999:
        break
    if busca >= len(Todos) or busca < 0:
        print(f'Erro! Não existe jogador com código {busca+1}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {Todos[busca]["Nome"]}')
        for c, k in enumerate(Todos[busca]["Gols"]):
            print(f' No jogo {c+1} fez {k} gols.')
    print('-'*40)
print('<<Volte Sempre!>>')


