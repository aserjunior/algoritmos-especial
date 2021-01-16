def main():
    salario = float(input('Insira o valor do salário: '))


    if salario > 0 and salario <= 400.00:
        aumento = 15
        ganho = (salario * aumento) / 100
        novo_salario = ganho + salario
        print(f'Novo salario: {novo_salario: .2f}')
        print(f'Reajuste ganho: {ganho: .2f}')
        print(f'Em percentual: {aumento}%')
    elif salario >= 400.01 and salario <= 800.00:
        aumento = 12
        ganho = (salario * aumento) / 100
        novo_salario = ganho + salario
        print(f'Novo salario: {novo_salario: .2f}')
        print(f'Reajuste ganho: {ganho: .2f}')
        print(f'Em percentual: {aumento}%')
    elif salario >= 800.01 and salario <= 1200.00:
        aumento = 10
        ganho = (salario * aumento) / 100
        novo_salario = ganho + salario
        print(f'Novo salario: {novo_salario: .2f}')
        print(f'Reajuste ganho: {ganho: .2f}')
        print(f'Em percentual: {aumento}%')
    elif salario >= 1200.01 and salario <= 2000.00:
        aumento = 7
        ganho = (salario * aumento) / 100
        novo_salario = ganho + salario
        print(f'Novo salario: {novo_salario: .2f}')
        print(f'Reajuste ganho: {ganho: .2f}')
        print(f'Em percentual: {aumento}%')
    elif salario > 2000.00: 
        aumento = 4
        ganho = (salario * aumento) / 100
        novo_salario = ganho + salario
        print(f'Novo salario: {novo_salario: .2f}')
        print(f'Reajuste ganho: {ganho: .2f}')
        print(f'Em percentual: {aumento}%')

    
main()