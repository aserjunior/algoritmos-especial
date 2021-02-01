def main():
    X = [''] * 10
    #contador = 0

    for i in range(len(X)):
        numero = int(input('Insira um número: '))
        if numero <= 0:
            print(f'X[{i}] = 1')
        else:
            print(f'X[{i}] = {numero}')
    
    
    #Esse for é utilzado para printar o vetor completo já alterado pelo for acima
    #Caso ele seja usado, coloque # nos dois prints acima e retire o # do contador
    #for item in X:
        #print(f'X[{contador}] = ', item )
        #contador += 1
        


main()