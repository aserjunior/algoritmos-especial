def main():
    #entrada
    codigo_1 = int(input('Insira o código da peça 1: '))
    numero_1 = int(input('Insira o número da peça 1: '))
    valor_1 = float(input('Insira o valor da peça 1: '))

    codigo_2 = int(input('Insira o código da peça 2: '))
    numero_2 = int(input('Insira o número da peça 2: '))
    valor_2 = float(input('Insira o valor da peça 2: '))

    #processamento
    valor_pago1 = numero_1 * valor_1
    valor_pago2 = numero_2 * valor_2

    valor_pago_total = valor_pago1 + valor_pago2
 
    #saída
    print(f'VALOR A PAGAR = {valor_pago_total}')


main()