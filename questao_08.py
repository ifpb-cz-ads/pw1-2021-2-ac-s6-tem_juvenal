dividendo = int(input('Dividendo: '))
divisor = int(input('Divisor: '))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1

resto = x
print('%d / %d = %d(quociente) %d(resto)' % (dividendo, divisor, quociente, resto))