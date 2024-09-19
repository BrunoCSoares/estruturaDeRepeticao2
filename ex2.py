'''
Escreva um algoritmo que solicite dois números e devolva quantos pares e
ímpares há entre esses dois números. Exemplo: entre 7 e 10 há 2 números
pares e 2 números ímpares
'''

num1 = int(input("Insira um número inteiro: "))
num2 = int(input("Insira um número inteiro: "))
pares = 0
impares = 0

for cont in range(num1,num2+1):
    if cont%2 == 0:
        pares += 1
    else:
        impares += 1

print(f"entre o número {num1} e {num2} há {pares} números pares")
print(f"entre o número {num1} e {num2} há {impares} números ímpares")