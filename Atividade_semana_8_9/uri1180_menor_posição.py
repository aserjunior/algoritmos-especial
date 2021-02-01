def main():
    N = int(input('Escolha o tamanho do vetor: '))
    X = [''] * N
    contador = 0
    menor = 0
    posiçao = 0
    
    
    if N > 1 and N < 1000:
        valores = input(f'Insira {N} valores que irão para dentro do vetor: ').split(' ')
        while contador < N:
           X[contador] = int(valores[contador])
           contador += 1
        print(X)
        menor = X[N - 1]
    
    
    for i in range(len(X)):
        if X[i] < menor:
            menor = X[i]
            posiçao = i
    

    print(f'Menor valor: {menor}\nPosição: {posiçao}')
        
        
main()