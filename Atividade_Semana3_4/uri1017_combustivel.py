def main():
    #entrada
    
    tempo = int(input('Insira o tempo em Horas: '))
    velocidada_media = int(input('Insira a velocidade média em Km/h: '))
    km_l = 12

    #processamento

    km_rodados = calcular_km(velocidada_media, tempo)
    total_litros = calcular_litros(km_rodados, km_l)

    #saída

    print(f'{total_litros: .3f}')
    

def calcular_km(v, t):
    calcular = v * t
    return calcular


def calcular_litros(km, l):
    calcular = km / l
    return calcular


main()