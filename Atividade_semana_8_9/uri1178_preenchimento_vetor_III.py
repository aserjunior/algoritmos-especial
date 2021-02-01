def main():
    X = float(input('Insira um valor: '))
    N = [''] * 100
    Z = 0
    contador = 0
    

    for i in range(len(N)):
       N[i] = X
       X = X / 2
    

    for i in range(len(N)):
        print(f'N[{i}] = ', N[i])


main()