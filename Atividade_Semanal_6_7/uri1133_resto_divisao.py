def main():
    X = 0
    Y = 0
    contador = 0
    soma = 0
    
    
    while contador < 2:
        valor = int(input('Insira um valor inteiro: '))
        contador += 1
        if contador == 1:
            X = valor
        if contador == 2:
            Y = valor
            while X < Y:
                cinco = div_5(X)
                X += 1
                if cinco == 0:
                    descarte = cinco
                else:
                    print(cinco)


def div_5(X):
    calculo = X % 5
    if calculo == 2 or calculo == 3:
        return X
    else:
        return 0


main()