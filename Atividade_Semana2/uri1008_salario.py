def main():
    #entrada
    num = int(input('Insira o número do funcionário: '))
    horas_trab = int(input('Insira as horas trabalhadas do funcionário: '))
    valor_hora = float(input('Insira o quanto o funcionário recebe por hora: '))

    #processamento
    salario = horas_trab * valor_hora

    #saída
    print(f'NÚMERO = {num} \nSALÁRIO = R$ {salario}')


main()