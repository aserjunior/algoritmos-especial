def main():
    max = 2
    min = 0
    soma = 0


    while min < max:
        nota = float(input('Insira a nota: '))
        
        
        if nota > 10 or nota < 0:
            print('nota invalida')
        else:
            min += 1
            soma += nota
        
        
        if min == max:
            media = calc_media(soma)
            print(f'media = {media}')


def calc_media(soma):
    calculo = soma / 2
    return calculo


main()