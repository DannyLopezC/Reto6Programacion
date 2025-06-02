i = float(input("ingrese un numero de 2 a 50: "))
divisor = 1
while divisor <= i:
    if i % divisor == 0:
        print(divisor)
    divisor += 1
