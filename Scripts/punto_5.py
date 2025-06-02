# funcion main
if __name__ == "__main__":
    # pedir un numero i y lo casteamos a flotante
    i = float(input("ingrese un numero de 2 a 50: "))
    # iniciamos los divisores a imprimir en 1 porque es el minimo divisor posible
    divisor = 1
    # mientras el divisor sea menor o igual al numero miramos si es divisor de i y lo imprimimos
    while divisor <= i:
        # sacamos el residuo de i / divisor para saber si es divisor
        if i % divisor == 0:
            print(divisor)
        # actualizacion de variable
        divisor += 1
