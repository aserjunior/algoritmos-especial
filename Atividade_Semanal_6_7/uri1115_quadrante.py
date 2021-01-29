def main():
    X = 1
    Y = 1


    while X != 0 and Y != 0:
        pontos = input('Insira as coordenadas de X e Y: ').split(' ')
        X = int(pontos[0])
        Y = int(pontos[1])


        if X > 0 and Y > 0:
            print('primeiro')
        elif X < 0 and Y > 0:
            print('segundo')
        elif X < 0 and Y < 0:
            print('terceiro')
        elif X > 0 and Y < 0:
            print('quarto')
        elif X == 0 or Y == 0:
            break 

    
main()