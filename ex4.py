'''
Escreva um programa para calcular o fatorial de um número n digitado pelo
usuário. Por exemplo: n = 5 fatorial = 5 x 4 x 3 x 2 x 1 = 120. OBS: utilize o
“for”.
'''

n = int(input("Digite um número inteiro: "))
fat = n

for i in range(1,n):
    fat += fat*(n-(i+1))
print(fat)