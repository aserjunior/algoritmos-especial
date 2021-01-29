def main():
    triangulo = input('Insira a medida dos lados do triângulo: ').split(' ')
    a = float(triangulo[0])
    b = float(triangulo[1])
    c = float(triangulo[2])
    A, B, C = sorted([a, b, c], reverse=True)
    tipo(A, B, C)


def tipo(A, B, C):
    if A >= B + C:
        print('NAO FORMA TRIANGULO')
    elif A ** 2 == B ** 2 + C ** 2:
        print('TRIANGULO RETANGULO')
    elif A ** 2 > B ** 2 + C ** 2:
        print('TRIANGULO OBTUSANGULO')
    elif A ** 2 < B ** 2 + C ** 2:
        print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')


main()