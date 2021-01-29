def main():
    max = 100
    contador = 0
    valor_max = 0
    posiçao = 0


    while contador < max:
        valor = int(input('Insira o valor inteiro: '))
        if valor_max < valor:
            valor_max = valor
            posiçao = contador + 1
        contador += 1


    print(f'>>> {valor_max}\n>>> {posiçao}')


main()