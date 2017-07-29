#!/usr/bin/python3
#Solicite os números a ser calculados

op = ''

while op.upper() != 'SAIR':


    n1 = int(input("Informe um valor: "))
    n2 = int(input("Informe outro valor: "))

# Solicite a operação
    op = input("Informe a operação a ser executada[+,-,*,/]: ")

# CONDIÇÃO CASO SEJA SOMA
    if op == "+":
        print(n1 + n2)

# Condição caso seja subtração
    elif op == "-":
        print(n1 - n2)

# Condição caso seja multiplicação
    elif op == "*":
        print(n1 * n2)

# Condição caso seja divisão
    elif op == "/":
        print(n1 / n2)
    
    elif op.upper() == 'SAIR':
        continue

# Caso não seja nenhuma opção válida
    else:
        print("Opção inválida")

