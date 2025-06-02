# funcion main
if __name__ == "__main__":
    # inicializamos i
    i = 0
    # mientras i sea menor a 1000 imprimimos los impares
    while i < 1000:
        # actualizacion de variable
        i += 1
        # residuo diferente de 0 para saber si es impar
        if i % 2 != 0:
            print(i)

    # reiniciamos i en 0
    i = 0
    # mientras i sea menor a 1000 imprimimos los pares
    while i < 1000:
        # actualizacion de variable
        i += 1
        # residuo 0 para saber si es par
        if i % 2 == 0:
            print(i)
