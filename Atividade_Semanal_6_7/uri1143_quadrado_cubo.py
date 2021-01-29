def main():
    N = int(input('Insira a quantidade de linhas: '))
    inicio = 1
    contador = 0


    while contador < N:
        if N < 1 or N > 1000:
            break
        quadrado = inicio ** 2
        cubo = inicio ** 3
        print(f'{inicio} {quadrado} {cubo}')
        inicio += 1
        contador += 1


main()