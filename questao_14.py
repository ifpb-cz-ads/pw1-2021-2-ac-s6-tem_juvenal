#Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
#Utilize a tabela de códigos abaixo para obter o preço de cada produto:

contaApagar = 0

while True:
    cod = int(input("Código da mercadore [0 para sair!]"))
    preco = 0
    if cod == 0:
        break
    elif cod == 1:
        preco = 0.50
    elif cod == 2:
        preco = 1.00
    elif cod == 3:
        preco == 4.00
    elif cod == 5:
        preco = 7.00
    elif cod == 9:
        preco = 8.00
    else:
        print("Código invalido!")
    if preco !=0:
        quantidade = int(input("Quantidade: "))
        contaApagar = contaApagar + (preco * quantidade)

print(f"Total a pagar R${contaApagar:8.2f}")



