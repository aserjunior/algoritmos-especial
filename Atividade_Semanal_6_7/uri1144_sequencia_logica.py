def main():
    numero = int(input('Digite um número inteiro: '))
    i = 1


    while i <= numero :
        print(str(int(i)) + ' ' + str(int(i * i)) + ' ' + str(int(i * i * i)))
        print(str(int(i)) + ' ' + str(int(i * i + 1)) + ' ' + str(int(i * i * i + 1)))
        i = i + 1


main()