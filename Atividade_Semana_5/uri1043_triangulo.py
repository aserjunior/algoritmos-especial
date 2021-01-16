def main():
    A = float(input('Insira um valor: '))
    B = float(input('Insira um valor: '))
    C = float(input('Insira um valor: '))
    

    if A > B > C or A > C > B:
        soma = B + C
        if soma > A:
            perimetro = A + B + C
            print(f'Perimetro = {perimetro: .1f}')
        elif soma <= A:
            area = ((A + B) * C) / 2
            print(f'Area = {area: .1f}')
    elif B > A > C or B > C > A:
        soma = A + C
        if soma > B:
            perimetro = A + B + C
            print(f'Perimetro = {perimetro: .1f}')
        elif soma <= B:
            area = ((A + B) * C) / 2
            print(f'Area = {area: .1f}')
    elif C > B > A or C > A > B:
        soma = B + C
        if soma > C:
            perimetro = A + B + C
            print(f'Perimetro = {perimetro: .1f}')
        elif soma <= C:
            area = ((A + B) * C) / 2
            print(f'Area = {area: .1f}')


main()            