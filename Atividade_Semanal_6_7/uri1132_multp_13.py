def main():
    X = 0
    Y = 0
    contador = 0
    soma = 0
    
    
    while contador < 2:
        valor = int(input('Insira um valor inteiro: '))
        contador += 1
        if contador == 1:
            X = valor
        if contador == 2:
            Y = valor
            while X <= Y:
                treze = mult_13(X)
                soma += treze
                X += 1           
            print(soma)
            

def mult_13(min):
    calculo = min % 13
    if calculo == 0:
        return 0
    else:
        return min


main()