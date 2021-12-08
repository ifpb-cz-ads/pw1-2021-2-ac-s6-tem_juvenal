valor = float(input("Inicial: "))
taxa = float(input("Taxa:"))
cont = 1
saldo = valor
while cont <= 12:
    valorM = float(input(f"Insira o valor do {cont}° mês:"))
    saldo = saldo + (saldo * (taxa / 100)+valorM)
    print(f"{cont}° Saldo: R${saldo:5.2f}.")
    cont = cont + 1
print(f"O valor obtido: R${saldo-valor:8.2f}.")