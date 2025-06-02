if __name__ == "__main__":
    n = int(input("Inserte un numero natural n: "))
    while n >= 2:
        if n % 2 == 0:
            print(n)
        n -= 1
