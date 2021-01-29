def main():
    X = 1
    contador = 0


    while contador < X:
        X = int(input('\nsequência: '))
        for i in range(contador + 1, X+1):
            print(i, end=(' '))
        while contador == X:
            contador = 0
            if X == 0:
                break


main()