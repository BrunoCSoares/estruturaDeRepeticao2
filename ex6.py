'''
Faça um programa que solicite ao usuário 15 números positivos e conte
quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-
100].
'''

num = 0
int1 = 0
int2 = 0
int3 = 0
int4 = 0

for i in range(15):
    num = int(input("Digite um número positivo: "))
    if 0 <= num <= 25:
        int1 += 1
    elif 26 <= num <= 50:
        int2 += 1
    elif 51 <= num <= 75:
        int3 += 1
    elif 76 <= num <= 100:
        int4 += 1

print(f"{int1} números estão no intervalo [0-25]")
print(f"{int2} números estão no intervalo [26-50]")
print(f"{int3} números estão no intervalo [51-75]")
print(f"{int4} números estão no intervalo [76-100]")