def main():
    #entrada

    x1 = float(input('Insira o valor de x1: '))
    y1 = float(input('Insira o valor de y1: '))
        
    x2 = float(input('Insira o valor de x2: '))
    y2 = float(input('Insira o valor de y2: '))

    #processamento

    distancia = calculo_distancia(x1, y1, x2, y2)

    #saída

    print(f'{distancia: .4f}')


def calculo_distancia(x1, y1, x2, y2):
    calculo = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    return calculo


main()




