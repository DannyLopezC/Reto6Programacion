if __name__ == "__main__":
    n = int(input("Inserte un numero natural n: "))
    resultado = n
    while n > 1:
        if n > 1:
            resultado *= n-1

        n -= 1

    print("el factorial es: " + str(resultado))
