def main():
    #entrada
    nome = str(input('Insira o nome do vendedor: '))
    salario_fixo = float(input('Insira o salário fixo do vendedor: '))
    total_vendas = float(input('Insira o total de vendas do mês: '))

    #processamento
    salario_total = salario_fixo + (0.15 * total_vendas)

    #saída
    print(f'SALÁRIO TOTAL = {salario_total}')


main()