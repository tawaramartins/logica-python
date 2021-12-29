# Crie um programa que recebe um numero e imprime o seu fatorial

numero = int(input("Digite um numero: "))
if numero > 0:
  fatorial = 1
for item in range(1, numero + 1):
  fatorial = fatorial * item 
print(fatorial)