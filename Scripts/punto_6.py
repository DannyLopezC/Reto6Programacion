# esta funcion recibe un numero entero y te devuelve True si es primo y False si no es primo
def es_primo(numero: int) -> bool:
    # si es menor o igual a uno no es primo retornamos False
    if numero <= 1:
        return False
    # para que sea primo no tiene que poder dividirse entre otro numero diferente a el mismo y el 1
    # por lo que iniciamos i en 2 para dividir el numero y mirar si i es divisor
    i = 2
    # mientras i sea menor al numero sacamos el residuo para saber si es divisor, si alguno es divisor retornamos False
    while i < numero:
        # si el residuo es 0 entonces es divisor
        if numero % i == 0:
            return False
        # actualizacion de variable
        i += 1

    # si ningun numero dividio al numero entonces retornamos True pues es primo
    return True


# funcion main
if __name__ == "__main__":
    # iniciamos el i en 0 para sacar los numeros que sean primos desde 0 hasta 100
    i = 0
    # mientras i sea menor o igual a 100 miramos si el numero es primo y lo imprimimos
    while i <= 100:
        # si es primo lo imprimimos
        if es_primo(i):
            print(i)
        # actualizacion de variable
        i += 1
