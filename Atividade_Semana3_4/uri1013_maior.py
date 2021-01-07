def main():
    #entrada

    A = int(input('Insira um valor para A: '))
    B = int(input('Insira um valor para B: '))
    C = int(input('Insira um valor para C: '))

    #processamento

    maior_A_B = eh_maior_AB(A, B)
    maior_C = checar_maior(maior_A_B, C)
    
    #saída

    if maior_A_B > maior_C:
        print(f'{maior_A_B: .0f} eh o maior')
    else: 
        maior_C > maior_A_B
        print(f'{maior_C: .0f} eh o maior')


def eh_maior_AB(a, b):
    calculo = (a + b + abs(a - b)) / 2
    return calculo


def checar_maior(maior_A_B, C):
    calculo = (maior_A_B + C + abs(maior_A_B - C)) / 2
    return calculo
    

main()