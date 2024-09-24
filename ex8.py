'''
Foi feita uma estatística nas 4 cidades da região Sudeste do Brasil para coletar
dados sobre acidentes de trânsito. Escreva um programa em Python que
solicite ao usuário os seguintes dados:
- nome da cidade
- número de veículos de passeio (em 2023)
- número de acidentes de trânsito com vítimas (em 2023)
Ao final do programa, exiba:
a) qual o maior e o menor índice de acidentes de trânsito e a que
cidades pertencem
b) qual a média de veículos nas cidades da região Sudeste
c) qual a média de acidentes com vítimas na cidade de São Paulo
'''

nomeCidade = [None] * 4
numCarros = [None] * 4
numVitimas = [None] * 4

for i in range(4):
    cidade = input("Insita o nome da cidade: ")
    carros = int(input("Insira o número de carros de passeio nesta cidade: "))
    vitimas = int(input("Insira o número de acidentes de trânsito com vítimas: "))
    nomeCidade[i] = cidade
    numCarros[i] = carros
    numVitimas[i] = vitimas
    print("\n")

maiorIndice = numVitimas[0]
for i in range(3):
    if numVitimas[i] > numVitimas[i+1] and numVitimas[i] > maiorIndice:
        maiorIndice = numVitimas[i]
    elif numVitimas[i+1] > maiorIndice:
        maiorIndice = numVitimas[i+1]

menorIndice = numVitimas[0]
for i in range(3):
    if numVitimas[i] < numVitimas[i+1] and numVitimas[i] < menorIndice:
        menorIndice = numVitimas[i]
    elif numVitimas[i+1] < menorIndice:
        menorIndice = numVitimas[i+1]

print(f"O maior indice de acidentes é {maiorIndice}")
print(f"O menor indice de acidentes é {menorIndice}")

mediaCarros = 0
for i in range(4):
    mediaCarros += numCarros[i]/4

print(f"A média de carros na região sudeste é {mediaCarros}")

SpVitimas = "sp"
for i in range(4):
    if nomeCidade[i][0] == "s":
        SpVitimas = numVitimas[i]

if SpVitimas == "sp":
    print("SP não encontrado")
else:
    print(f"O número de vítimas em SP é {SpVitimas}")