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
        

        while min == max:
            check = int(input('novo calculo (1-sim 2-nao) ? : '))
            
            
            if check == 2:
                break
            elif check == 1:
                soma = 0
                min = 0


def calc_media(soma):
    calculo = soma / 2
    return calculo


main()