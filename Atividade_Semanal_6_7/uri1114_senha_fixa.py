def main():
    senha = 2002
    X = 0
    while senha != X:
        X = int(input('Insira a senha: '))
        if X != senha:
            print('>>> Senha Invalida')
        elif X == senha:
            print('>>> Acesso Permitido')

main()