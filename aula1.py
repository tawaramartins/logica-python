# Problema 1
# Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

salario_mensal = input("Qual e o seu salario? ")
horas_trabalhadas = input("Quantas horas voce trabalha por mes? ")
valor_hora = int(salario_mensal) / int(horas_trabalhadas)
print(valor_hora)