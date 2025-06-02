def es_primo(numero):
    if numero <= 1:
        return False
    i = 2
    while i < numero:
        if numero % i == 0:
            return False
        i += 1

    return True


i = 0
while i <= 100:
    if es_primo(i):
        print(i)
    i += 1
