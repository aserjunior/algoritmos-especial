def main():
#entrada
    lanche = int(input('Insira o código do pedido: '))
    quantidade = int(input('Insira quantos pedidos vai querer: '))
    

#processamento
    validar = validar_lanche(lanche)
    valor_final = valor_lanche(validar, quantidade)


#saída
    print(f'Total: R${valor_final: .2f}')

  
def validar_lanche(lanche):
    if lanche is 1:
        return 4.00
    elif lanche is 2:
        return 4.50
    elif lanche is 3:
        return 5.00
    elif lanche is 4:
        return 2.00
    elif lanche is 5:
        return 1.50


def valor_lanche(codigo, quantidade):
        calculo = codigo * quantidade
        return calculo


main()