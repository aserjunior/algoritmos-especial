def main():
    X = 1
    Y = 0
    

    while X != Y:
        valor = input('Insira os valores de X e Y: ').split(' ')
        X = int(valor[0])
        Y = int(valor[1])


        if X > Y:
            print('Decrescente')
        elif X < Y:
            print('Crescente')


main()