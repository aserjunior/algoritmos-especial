def main():
    N = [''] * 20
    contador = 19

    for i in range(len(N)):
        numero = int(input('Insira o número: '))
        if i >= 0:
            print(f'N=[{contador}] = {numero}')
            contador -= 1

    
    
main()
        