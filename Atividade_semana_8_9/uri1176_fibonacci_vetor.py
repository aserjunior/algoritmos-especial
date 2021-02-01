def main():
    X = 0
    Y = 1
    T = int(input('Insira o número de casos teste: '))
    contador = 0
    fib = [''] * 60


    for i in range(len(fib)):
        fib[i] = X
        soma = X + Y
        X = Y
        Y = soma
    #print(fib)


    while contador < T:
        escolha = int(input('Insira a posição desejada para saber qual valor se refere na sequência de fibonacci:'))
        contador += 1
        print(f'Fib({escolha}) = {fib[escolha]}' )


main()