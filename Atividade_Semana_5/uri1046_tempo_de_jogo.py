def main():
    A = int(input('Insira a hora inicial: '))
    B = int(input('Insira a hora final: '))


    if A == B:
        print('O JOGO DUROU 24 HORA(S)')
    elif A > B:
        inicial = 23 - A
        final = B + 1
        duracao = inicial + final
        print(f'O JOGO DUROU {duracao} HORA(S)')  
    elif B > A:
        duracao = B - A
        print(f'O JOGO DUROU {duracao} HORAS(S)')


main()