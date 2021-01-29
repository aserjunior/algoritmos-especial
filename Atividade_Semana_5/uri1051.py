def main():
    salario = float(input('Salario: '))


    if salario <= 2000:
        print('Isento')
    elif salario <= 3000:
        imposto = 0.08 * (salario - 2000)
        print(f'R$ {imposto: .2f}')
    elif salario <= 4500:
        imposto = 0.08 * 1000 + 0.18 * (salario - 3000)
        print(f'R$ {imposto: .2f}')
    else:
        imposto = 0.08 * 1000 + 0.18 * 1500 + 0.28 * (salario - 4500)
        print(f'R$ {imposto: .2f}')


main()