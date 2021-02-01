def main():
    numero = int(input('Insira o número: '))
    N = [''] * 10
    contador = 0

    for i in range(len(N)):
        if i < 1:
            print(f'N[{i}] = {numero}')
        else:
            numero = numero * 2
            print(f'N[{i}] = {numero}')


main()