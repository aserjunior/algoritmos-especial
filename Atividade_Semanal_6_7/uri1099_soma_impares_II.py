def main():
    teste = int(input('Insira a quantidade de testes a serem feitos: '))
    contador = 0
    soma = 0


    while contador < teste:
        valores = input('Insira os dois valores X e Y: ').split(' ')
        contador += 1
        n_1 = int(valores[0])
        n_2 = int(valores[1])
        
        
        if n_1 < n_2:
            while n_1 < n_2 - 1:
                n_1 += 1
                primos = primo(n_1)
                soma += primos
            print(soma)
            if soma > 0:
                    soma = 0


        elif n_1 > n_2:
            while n_2 < n_1 - 1:
                n_2 += 1
                primos = primo(n_2)
                soma += primos
            print(soma)
            if soma > 0:
                soma = 0
        
        
        elif n_1 == n_2:
            print('0')
            

def primo(valor):
    calculo = (valor + 1) % 2
    if calculo == 0:
        return valor
    else:
        return 0
    

main()