def main():
    pares = int(input('Insira a quantidade de pares que serão utilizados: '))
    contador = 0


    while contador < pares:
        valores = input('Insira os valores da divisão entre X e Y: ').split(' ')
        X = int(valores[0])
        Y = int(valores[1])
        divisao = div(X, Y)
        contador += 1
        print(divisao)


def div(X, Y):
    if  Y == 0:
        return 'Divisão impossivel'
    else:
        calculo = X / Y
        return calculo
    
   
main()