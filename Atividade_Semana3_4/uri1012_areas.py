def main():
    #entrada

    A = float(input('Insira o valor de A: '))
    B = float(input('Insira o valor de B: '))
    C = float(input('Insira o valor de C: '))
    pi = 3.14159

    #processamento

    area_triangulo = calculo_area_tri(A, C)
    area_circulo = calculo_circulo(pi, C)
    area_trapezio = calculo_trapezio(A, B, C)
    area_quadrado = calculo_quadradado(B)
    area_retangulo = calculo_retangulo(A, B)

    #saída

    print(f'TRIANGULO: {area_triangulo: .3f}')
    print(f'CIRCULO: {area_circulo: .3f}')
    print(f'TRAPEZIO: {area_trapezio: .3f}')
    print(f'QUADRADO: {area_quadrado: .3f}')
    print(f'RETANGULO: {area_retangulo: .3f}')


def calculo_area_tri(Base, Altura):
    calculo = (Base * Altura) / 2
    return calculo


def calculo_circulo(pi, raio):
    calculo = pi * raio ** 2
    return calculo


def calculo_trapezio(base1, base2, altura):
    calculo = ((base1 + base2) * altura) / 2
    return calculo


def calculo_quadradado(lado):
    calculo = lado ** 2
    return calculo


def calculo_retangulo(lado1, lado2):
    calculo = lado1 * lado2
    return calculo


main()