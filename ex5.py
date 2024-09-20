'''
Escreva um programa que calcule o somatório de todos os números pares em
um intervalo definido pelo usuário. Ex: para inicio = 2 e fim = 10 o somatório é
2+4+6+8+10. OBS: utilize o “for”.
'''

numI = int(input("Informe o número inicial: "))
numF = int(input("Informe o número final: "))
soma = 0

for i in range(numI,numF+1):
    if i % 2 == 0:
        soma += i
    print(soma)