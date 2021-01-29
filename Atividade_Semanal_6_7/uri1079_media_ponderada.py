def main():
    casos = int(input('Escolha o número de casos de teste: '))
    peso_1 = 2
    peso_2 = 3
    peso_3 = 5
    contador = 0


    while contador < casos:
        valores = input('Coloque os 3 valores reais: ').split(' ')
        media = calcular_media(valores, peso_1, peso_2, peso_3)
        print(f'{media: .1f}')
        contador += 1


def calcular_media(valores, peso_1, peso_2, peso_3):
    calculo = (peso_1 * float(valores[0]) + peso_2 * float(valores[1]) + float(valores[2]) * peso_3) / (peso_1 + peso_2 + peso_3)
    return calculo 


main()