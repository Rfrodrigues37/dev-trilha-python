#Ler dois numeros

number1 = int(input("DIgite o primeiro numero = "))
number2 = int(input("DIgite o segundo  numero = "))

if number1 > number2:
    maior = number1
else:
    maior = number2
print("O maior numero é = ", maior)