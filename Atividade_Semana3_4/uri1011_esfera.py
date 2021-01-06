def main():
    #entrada
    
    raio = int(input('Insira o valor do raio: '))
    pi = 3.14159

    #processamento

    volume = calcular_volume(pi, raio)


    #saída

    print(f'VOLUME = {volume}')


def calcular_volume(pi, raio):
    calculo = (4/3) * pi * raio ** 3 
    return calculo 


main()