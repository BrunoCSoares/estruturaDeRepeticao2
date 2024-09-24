'''
Faça um programa em Python que solicite ao usuário os seguintes dados para
10 pessoas:
- nome
- idade
- gênero (masculino ou feminino)
- cor dos olhos
- cor dos cabelos
Ao final o exiba as seguintes informações:
- o nome e a idade da pessoa mais velha;
- o nome e a idade da pessoa mais jovem;
- a quantidade de pessoas do sexo feminino cuja idade está entre 18 e
35 anos (inclusive) e que tenham olhos verdes.
- a média de idade das pessoas que têm cabelos louros.
'''

nome = [None]*10
idade = [None]*10
genero = [None]*10
corOlhos = [None]*10
corCabelos = [None]*10
maisVelha = [None]*2
maisJovem = [None]*2

for i in range(10):
    nome[i] = input(f"Insira o nome da {i + 1}a. pessoa: ")
    idade[i] = int(input(f"Insira a idade da {i + 1}a. pessoa: "))
    genero[i] = input(f"Insira o gênero da {i + 1}a. pessoa [M/F]: ")
    corOlhos[i] = input(f"Insira a cor dos olhos da {i + 1}a. pessoa: ")
    corCabelos[i] = input(f"Insira a cor dos cabelos da {i + 1}a. pessoa: ")
    print("\n")

maisJovem[0] = nome[0]
maisJovem[1] = idade[0]
for i in range(9):
    if idade[i] < idade[i+1] and idade[i] < maisJovem[1]:
        maisJovem[0] = nome[i]
        maisJovem[1] = idade[i]
    elif idade[i+1] < maisJovem[1]:
        maisJovem[0] = nome[i+1]
        maisJovem[1] = idade[i+1]

maisVelha[0] = nome[0]
maisVelha[1] = idade[0]
for i in range(9):
    if idade[i] > idade[i+1] and idade[i] > maisVelha[1]:
        maisVelha[0] = nome[i]
        maisVelha[1] = idade[i]
    elif idade[i+1] > maisVelha[1]:
        maisVelha[0] = nome[i+1]
        maisVelha[1] = idade[i+1]

print(f"A pessoa mais velha é {maisVelha[0]} com {maisVelha[1]} anos de idade")
print(f"A pessoa mais jovem é {maisJovem[0]} com {maisJovem[1]} anos de idade")

pessoasEspecificas = 0
for i in range(10):
    if genero[i][0] == "f" and idade[i] >= 18 and idade[i] <= 35 and corOlhos[i][0] == "v":
        pessoasEspecificas += 1

print(f"A quantidade de pessoas do gênero feminino entre 18 e 35 anos com olhos verde é {pessoasEspecificas}")

qtdLouros = 0
somaIdadeLouros = 0
for i in range(10):
    if corCabelos[i][0] == "l":
        qtdLouros += 1
        somaIdadeLouros += idade[i]
mediaIdadeLouros = somaIdadeLouros / qtdLouros

print(f"A média da idade de pessoas com cabelos louros é {mediaIdadeLouros:.0f} anos")