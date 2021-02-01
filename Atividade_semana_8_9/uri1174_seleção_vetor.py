def main():
    A = [''] * 100


    for i in range(len(A)):
        numero = float(input('Insira um número '))
        if numero <= 10:
            print(f'A[{i}] = {numero}')
        else:
            pass


main()
