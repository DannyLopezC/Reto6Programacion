# funcion main
if __name__ == "__main__":
    # pedir un numero n y lo casteamos a entero
    n = int(input("Inserte un numero natural n: "))
    # inicializamos resultado como la variable donde se guardara el resultado
    resultado = n
    # si n es 0 entonces el factorial es 1
    if n == 0:
        resultado = 1

    # mientras n sea > 1 multiplicamos resultado por el n-1
    while n > 1:
        n -= 1
        resultado *= n

    # si el numero era negativo el factorial no esta definido
    if resultado >= 1:
        print("el factorial es: " + str(resultado))
    else:
        print("el factorial de numeros negativos no esta definido")
