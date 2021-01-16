def main():
    A = int(input('Insira um valor: '))
    B = int(input('Insira um valor: '))


    if A > B:
        verificar = A % B
        if verificar == 0:
            print('São Multiplos')
        elif verificar != 0:
            print('Não são Multiplos')
    elif B > A:
        verificar = B % A
        if verificar == 0:
            print('São Multiplos')
        elif verificar != 0:
            print('Não são Multiplos')


main()            