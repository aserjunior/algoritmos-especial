def main():
    grenal = 0
    empate = 0
    vit_G = 0
    vit_I = 0
    Gre = 0
    Int = 0
    contador = 0
    
    
    while contador < 1:
        jogo = input('Insira o resultado do jogo na ordem Gremio x Inter: ').split(' ')
        Gre = int(jogo[1])
        Int = int(jogo[0])
        if Gre == Int:
            empate += 1
            grenal += 1
            contador += 1
        elif Gre > Int:
            vit_G += 1
            grenal += 1
            contador += 1
        elif Int > Gre:
            vit_I +=1
            grenal += 1
            contador += 1


        while contador == 1:
            check = int(input('Novo grenal (1-sim 2-nao) ? :'))
            if check == 1:
                contador = 0
            elif check == 2:
                print(f'{grenal} grenais')
                print(f'Inter: {vit_I}')
                print(f'Gremio: {vit_G}')
                print(f'Empates: {empate}')
                if vit_G > vit_I:
                    print('gremio venceu mais')
                elif vit_I > vit_G:
                    print('inter venceu mais')
                break

                
main()