def main():
    N = int(input('Insira o valor de N: '))
    contador = 1


    while contador <= N:
        if N % contador == 0:
            print(contador)
        else:
            False
        contador += 1


main()