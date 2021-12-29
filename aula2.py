# Problema 2
# Encontre o maior entre dois numeros 

primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")
if int(primeiro_valor) > int(segundo_valor):
  print("O primeiro valor e o maior!")
elif primeiro_valor == segundo_valor:
  print("Os dois valores sao iguais!")
else:
  print("O segundo valor e maior!")