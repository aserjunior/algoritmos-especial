def main():
    A = int(input('Insira um valor: '))
    B = int(input('Insira um valor: '))
    C = int(input('Insira um valor: '))


    if A < B < C:
        print(f'{A}\n{B}\n{C}\n\n{A}\n{B}\n{C}')
    elif A < C < B:
        print(f'{A}\n{C}\n{B}\n\n{A}\n{B}\n{C}')
    elif B < A < C:
        print(f'{B}\n{A}\n{C}\n\n{A}\n{B}\n{C}')
    elif B < C < A:
        print(f'{B}\n{C}\n{A}\n\n{A}\n{B}\n{C}')
    elif C < A < B:
        print(f'{C}\n{A}\n{B}\n\n{A}\n{B}\n{C}')
    elif C < B < A:
        print(f'{C}\n{B}\n{A}\n\n{A}\n{B}\n{C}')


main()