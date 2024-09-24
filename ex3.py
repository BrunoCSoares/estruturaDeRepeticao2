'''
Desenvolva um programa para calcular a média salarial dos funcionários da
empresa XXX, para isso seu programa deverá solicitar o nome e salário dos 5
funcionários que trabalham nessa empresa. Ao final seu programa deverá
calcular a média dos salários e exibir na tela as seguintes informações: (use 2
casas decimais na exibição dos números)
o A média salarial dos funcionários da empresa XXX é _______
o O nome e o salário do funcionário que recebe o menor salário
o O nome e o salário do funcionário que recebe o maior salário
'''

nome = [None]*5
salario = [None]*5
somaSalarios = 0

for i in range(5):
    nome[i] = input(f"Informe o nome do {i+1}o. funcionário: ")
    salario[i] = float(input(f"Informe o salário de {nome[i]}: "))
    print("\n")
    somaSalarios += salario[i]
mediaSalarios = somaSalarios / 5

print(f"A média salarial dos funcionários da empresa FIAP é R${mediaSalarios:.2f}")

maiorSalario = salario[0]
for i in range(4):
    if salario[i] > salario[i+1] and salario[i] > maiorSalario:
        maiorSalario = salario[i]
        maiorAssalariado = nome[i]
    elif salario[i+1] > maiorSalario:
        maiorSalario = salario[i+1]
        maiorAssalariado = nome[i+1]
print(f"O maior salário é R${maiorSalario:.2f} do funcionário {maiorAssalariado}")


menorSalario = salario[0]
for i in range(4):
    if salario[i] < salario[i+1] and salario[i] < menorSalario:
        menorSalario = salario[i]
        menorAssalariado = nome[i]
    elif salario[i+1] < menorSalario:
        menorSalario = salario[i+1]
        menorAssalariado = nome[i+1]
print(f"O menor salário é R${menorSalario:.2f} do funcionário {menorAssalariado}")