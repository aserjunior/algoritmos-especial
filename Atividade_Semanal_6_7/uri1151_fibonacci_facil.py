def main():
    termo = int(input('Insira a quantidade de termos na sequência de Fibonacci: '))
    contador = 0
    X = 0
    Y = 1
    print(X, end=(' '))
    
    
    while contador < termo - 1:
        contador += 1
        soma = X + Y
        X = Y
        Y = soma
        print(X, end=(' '))

        
main()