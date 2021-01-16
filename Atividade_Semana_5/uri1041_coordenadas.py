def main():
    x = float(input('Insira o valor de x: '))
    y = float(input('Insira o valor de y: '))


    if x == 0 and y == 0:
        print('Origem')
    elif x > 0 and y > 0:
        print('Q1')
    elif x < 0 and y > 0:
        print('Q2')
    elif x < 0 and y < 0:
        print('Q3')
    elif x > 0 and y < 0:
        print('Q4')


main()