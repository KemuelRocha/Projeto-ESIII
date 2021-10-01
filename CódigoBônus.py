from time import sleep


def exemplo(): # Exemplo
    Jogador = dict()  # criação de um dicionário
    Todos = list()  # criação de uma lista
    Gols = list()  # criação de uma lista

    while True:  # Loop infinito
        Jogador.clear()  # Limpa tudo que está dentro do dicionário Jogador

        Jogador['Nome'] = str(input(
            'Nome do Jogador: ')).strip()  # Adiciona à chave Nome do dicionário Jogador, um valor que o usuário fornece
        # Função strip é usada para retirar espaços tanto do inicio tanto do fim.

        part = int(input(
            f'Quantas partidas {Jogador["Nome"]} Jogou? '))  # A variavél part recebe um valor inteiro fornecido pelo usuário

        for c in range(part):  # Loop for com um tamanho de part, que foi fornecido pelo usuário
            Gols.append(int(input(
                f' Quantos Gols na partida {c + 1}? ')))  # Adiciona na lista Gols um valor fornecido pelo usuário
        Jogador['Gols'] = Gols[:]  # Faz uma cópia da lista Gols para o dicionário com a chave Gols

        Jogador['Total'] = sum(Gols)  # Adiciona na chave do dicionário Jogador Total o somatório da lista gols

        Todos.append(Jogador.copy())  # A lsita Todos recebe uma copia de todo dicionário Jogador

        Gols.clear()  # Limpa a lista Gols
        while True:
            opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if opção in 'SN':  # Condição if que verifica se S ou N está dentro da variavel opção
                break
            else:
                print('ERRO! Digite Somente S ou N')
        if opção == 'N':  # Condição de parada para o cadastramento de jogadores
            break

    print('-=' * 30)
    print('-' * 40)
    print('cod ', end='')
    for i in Jogador.keys():  # loop nas chaves do dicionário
        print(f'{i:<15}', end='')
    print()
    print('-' * 40)
    for k, v in enumerate(Todos):  # Loop com enumeração dos valores que estão dentro da lista Todos
        print(f'{k:>3} ', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()
    while True:
        busca = int(input('Mostrar dados de qual jogador? (999 para parar):'))
        if busca == 999:
            break
        if busca >= len(Todos) or busca < 0:
            print(f'Erro! Não existe jogador com código {busca}!')
        else:
            print(f'-- LEVANTAMENTO DO JOGADOR {Todos[busca]["Nome"]}')
            for c, k in enumerate(Todos[busca]["Gols"]):
                print(f' No jogo {c + 1} fez {k} gols.')
        print('-' * 40)
    print('<<Volte Sempre!>>')




Menu = ['\033[0:32mPRINT', '\033[0:32mIF & ELSE', '\033[0:32mFOR', '\033[0:32mWHILE', '\033[0:32mDICIONÁRIO', '\033[0:32mLISTAS', '\033[0:32mALGUMAS FUNÇÕES EXTRAS', '\033[0:32mEXEMPLO', '\033[0:33mSAIR\033[m']
print('Escolha uma opção para que seja mostrado um exemplo:')

while True:
    print('-' * 20, 'Menu', '-'* 20)
    for n, i in enumerate(Menu):
        print(f'\033[4:31m{n+1}\033[m- {i} ')
    print('-'*50)
    while True:
        opção = input('').strip()[0]
        sleep(0.5)
        if opção in '0123456789':
            break
        else:
            print('ERRO! Opção invalida.')
    if opção == '9':
        print('Fim do Programa')
        break
    else:
        if opção == '1':
            print('print("O print é usado quando se quer mostrar algum texto para o usuário.")')
            sleep(2)
            Menu[0] = '\033[0:31mPRINT'
            
        elif opção == '2':
        print("""opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opção in 'SN':   # Condição if que verifica se S ou N está dentro da variavel opção
            break
        else:
            print('ERRO! Digite Somente S ou N')""")
            sleep(5)
            Menu[1] = '\033[0:31mIF & ELSE'
            
        elif opção == '3':
            print(""" for c, k in enumerate(Todos[busca]["Gols"]): # For em conjunto com o enumerate 
            para mostrar oque tem dentro da lista todos enumerando cada linha dela
            print(f' No jogo {c+1} fez {k} gols.')""")
            sleep(2)
            Menu[2] = '\033[0:31mFOR'
            
        elif opção == '4':
            print("""while True:         # Loop infinito 
            Onde sua condição de parada é o break""")
            sleep(2)
            Menu[3] = '\033[0:31mWHILE'
            
        elif opção == '5':
            print("""Jogador = dict()  # criação de um dicionário""")
            sleep(1)
            Menu[4] = '\033[0:31mDICIONÁRIO'
            
        elif opção == '6':
            print("""Todos = list()    # criação de uma lista""")
            sleep(1)
            Menu[5] = '\033[0:31mLISTAS'
            
        elif opção == '7':
            print("""   .strip() #É usa para eliminar espaços em branco do início  e do fim.
            input() #É a função usado pra recever dados que o usuário passa pelo teclado.
            .copy() #É uma função usada para se fazer a copia de uma variável
            .upper() #Função usada para deixar todas as letras de uma string maiúsculas
            len() #Função usada para mostrar a quantidade de valores que uma variavel possui
            enumerate() #Função usada para enumerar uma variavel, geralmente é usada no FOR
            append() #Função usada para adicionar valores dentro de listas 
            sum() #Função usada para somar todos os valores que estão dentro de uma vairável""")
            sleep(5)
            Menu[6] = '\033[0:31mALGUMAS FUNÇÕES EXTRAS'
            
        else:
            exemplo()
            sleep(2)
            Menu[7] = '\033[0:31mEXEMPLO'


