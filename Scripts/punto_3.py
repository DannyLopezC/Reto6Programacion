# funcion main
if __name__ == "__main__":
    # pedir un numero n y lo casteamos a entero
    n = int(input("Inserte un numero natural n: "))
    # mientras n sea mayor o igual a 2 imprimimos los pares de forma descendente
    while n >= 2:
        # residuo 0 para saber si es par
        if n % 2 == 0:
            print(n)
        # actualizacion de variable
        n -= 1
