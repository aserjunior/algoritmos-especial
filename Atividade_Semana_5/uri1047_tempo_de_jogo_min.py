def main():
    A = int(input('Insira a hora inicial: '))
    B = int(input('Insira o minuto inicial: '))
    C = int(input('Insira a hora final: '))
    D = int(input('Insira o minuto final: '))


    if A == C and B == D:
        print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    elif B > D:
        hora = (C - A) * 60
        minutos = D - B
        duracao_horas = (hora - (- minutos)) // 60
        duracao_min = (hora + minutos) % 60
        print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_min} MINUTO(S)')
    elif D > B:
        hora = C - A
        minutos = D - B
        print(f'O JOGO DUROU {hora} HORA(S) E {minutos} MINUTO(S)')


main()