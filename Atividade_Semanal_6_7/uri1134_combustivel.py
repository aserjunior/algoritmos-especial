def main():
    alcool = 0
    gas = 0
    diesel = 0
    contador = 0

    while contador < 1:
        produto = int(input('(1.Alcool 2.Gasolina.3.Diesel.4fim): '))
        if produto == 1:
            alcool += 1
            contador += 1
        elif produto == 2:
            gas += 1
            contador += 1
        elif produto == 3:
            diesel += 1
            contador += 1
        elif produto == 4:
            contador += 1
            break

        
        while contador == 1:
            check = int(input('(1.Alcool 2.Gasolina.3.Diesel.4fim): '))
            if check == 4:
                print('Muito Obrigado')
                print(f'Alcool: {alcool}')
                print(f'Gasolina: {gas}')
                print(f'Diesel: {diesel}')
                break
            elif check == 1:
                alcool += 1
                contador = 0
            elif check == 2:
                gas += 1
                contador = 0
            elif check == 3:
                diesel += 1
                contador = 0


main()