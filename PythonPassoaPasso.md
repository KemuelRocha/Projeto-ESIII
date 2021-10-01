![i](/imagem.png?raw=true)

O que aprenderemos: 
   * [Instalção](#Instalação)
   * [Configuração](#Configuração)
   * [Primeiro Programa](#PrimeiroPrograma)
   * [Comentários](#Comentarios)
   * [Nível iniciante](#NívelINiciante)
       * [Variáveis](#Variáveis)
   * [Nível intermediário](#NívelIntermerdiário)       
       * [If e Else](#IfeElse)
   * [Nível avançado](#NívelAvançado)   
        * [Funções](#Funções)
        * [Loops](#Loops)
   * [CódigoExtra](#CódigoExtra)

# Instalação


Tutorial para instalação


https://python.org.br/instalacao-windows/


Download do Python versão 3.9.7

https://www.python.org/downloads/


# Configuração 

Vídeo explicativo sobre a instalação do PyCharm 

https://www.youtube.com/watch?v=HNUq8X_0nlM

Configurando e instruindo como utilizar o PyCharm

https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html


# Primeiro programa

Mostraremos a seguir instruções de como realizar seu primeiro programa!

Escreva o código : 
```sh
print('Olá, mundo!')
```

Veja o código acessando também 

https://blog.betrybe.com/desenvolvimento-web/hello-world-ola-mundo/


# Comentários

Aprenderemos agora algumas formas de utilizar o comentário em pyhton

Notação Inline
```sh
print(teste) #a instrução atrás da cerquilha será interpretada
```
Notação Multilines
```sh
'''
toda informações contida entre 3 aspas SIMPLES
é considerada como caracteres que devem ser ignorados.
'''
```
Para mais informações, acesse
http://excript.com/python/comentarios-em-python.html


# Variáveis

Realizaremos agora a utilização de  variáveis em Python:
variável = expressão
```sh
'''
Exemplos:
k = 0  #k recebe o valor 0
a = 1 
A = 2
c = k + a + A   #c recebe os valores da soma de k, a e A
'''
```
Vale ressaltar que há distinção entre maiúsculo e minúsculo, como mostrado acima.

Para mais informações, acesse:
https://panda.ime.usp.br/panda/static/aulasPython/aula02.html


# If e Else
Visualizaremos a seguir as atribuições de IF, ELIF, ELSE:
Para o IF
```sh
b = 300
A = 200
if A > b:     #Condição IF
    print("A é maior do que b") 
  ```
O ELIF (ELSE + IF) é uma condição similar ao ELSE, entretando, ele necessita que seja transcrita outra condição em sequência (IF).
```sh
b = 300
A = 200
if A > b:       #Condição IF
    print("A é maior do que b") 
  
elif A == b:      #Confição ELIF, caso não entre no primeiro IF
    print("A é igual a b")
  ```

 Para o ELSE
```sh
b = 300
A = 200
if A > a:            #Condição IF
    print("A é maior do que b") 
  
elif A == a:         #Condição ELIF
    print("A é igual a b")

else:                #Condição ELSE
    print("A é menor a b")
  ```
  
  Para mais informações, técnicas e conceitos sobre, acesse: 
  https://www.w3schools.com/python/python_conditions.asp
  

# Loops

Agora veremos as estruturas de repetição, for, while, e while true: 

For
```sh
for i in range(5):
    print(i)
"""
0
1
2
3
4
"""
  ```
 While
 ```sh
 count = 0
while count <= 5:
    print(count)
    count += 1
    # 0 1 2 3 4 5
  ```
While True
 ```sh
while True:
   print('foo')
   # foo,foo,foo..
  ```
 Para mais informações sobre as estruturas de repetições estudadas, acesse: 
 http://devfuria.com.br/python/lacos-de-repeticao/
 https://realpython.com/python-while-loop/


# Código Extra 

Execute o código extra para consilidação da aprendizagem dos assuntos abordados, além de outros a conteúdos!!
