#Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero).
#No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.


cont = 0
soma = 0

while True:
     numero = int(input("Digite um número inteiro: "))
     if numero == 0 :
        break
     soma = soma + numero
     cont = cont + 1

print("Quantidade de números digitados: ",cont)
print("Soma: ",soma)
print(f"Média: {soma/cont:7.2f}")