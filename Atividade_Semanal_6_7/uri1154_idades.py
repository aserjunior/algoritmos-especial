def main():
    contador = 0
    idade = 0
    soma = 0
   
   
    while idade >= 0:
        idade = int(input('Insira a idade: '))     
        contador += 1
        soma += idade
        if idade < 0:
            soma -= idade
            media = calc_media(soma, contador)
            print(media)
            break


def calc_media(soma, contador):
    calculo = soma / (contador - 1)
    return calculo


main()