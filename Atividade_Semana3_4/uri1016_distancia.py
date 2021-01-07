def main():
    #entrada
    
    distancia = int(input('Insira a distancia em (Km): '))

    #processamento

    tempo_distan = calculo_distancia(distancia, 2)

    #saída

    print(f'{tempo_distan} minutos')


def calculo_distancia(Km, tempo):
    calculo = Km * tempo
    return calculo


main()