def main():
    #entrada
    A = float(input('Insira a nota A: '))
    B = float(input('Insira a nota B: '))
    C = float(input('Insira a nota C: '))

    pesoA = 2
    pesoB = 3
    pesoC = 5

    #processamento
    media = ((A * pesoA) + (B * pesoB) + (C * pesoC)) / (pesoA + pesoB + pesoC)
    
    #saída
    print(f'MEDIA = {media}')


main()