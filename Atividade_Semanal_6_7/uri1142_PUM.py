def main():
    N = int(input('Insira a quantidade de linhas: '))
    contador = 0
    inicio = 1
    

    while contador < N:
        print(f'{inicio} {inicio + 1} {inicio + 2} PUM')
        inicio += 4
        contador += 1


main()