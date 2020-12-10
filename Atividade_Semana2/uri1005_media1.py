def main():
    #entrada
    A = float(input('Insira a nota A: '))
    B = float(input('Insira a nota B: '))
    
    pesoA = 3.5
    pesoB = 7.5
    
    #processamento
    media = ((A * pesoA) + (B * pesoB)) / (pesoA + pesoB)

    #saída
    print(f'MEDIA = {media}')


main()