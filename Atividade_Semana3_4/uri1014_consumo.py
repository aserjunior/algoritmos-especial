def main():
    #entrada
    
    X = int(input('Insira a distância total percorrida (Km):'))
    Y = float(input('Insira o total de combustível gasto (L):'))

    #processamento

    consumo = calculo_consumo(X, Y)

    #saída

    print(f'{consumo: .3f} km/l')


def calculo_consumo(distancia, combustivel):
    calculo = distancia / combustivel 
    return calculo


main()