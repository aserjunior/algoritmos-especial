def main():

    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    n4 = float(input('Nota 4: '))

    peso_1 = 2
    peso_2 = 3
    peso_3 = 4
    peso_4 = 1


    media = calculo_media(n1, n2, n3, n4, peso_1, peso_2, peso_3, peso_4)
    
    
    if media >= 7.0:
        print(f'Media: {media: .1f}')
        print('Aluno aprovado.')
    elif media < 5:
        print(f'Media: {media: .1f}')
        print('Aluno reprovado.')
    elif media >= 5 and media <= 6.9:
        print(f'Media: {media: .1f}')
        print('Aluno em exame.')
        exame = float(input('Nota do exame: '))
        print(f'Nota do exame: {exame: .1f}')
        media_2 = (exame + media) / 2
        if media_2 >= 5.0:
            print('Aluno aprovado.')
            print(f'Media final: {media_2: .1f}')
        elif media_2 < 4.9:
            print('Aluno reprovado.')


def calculo_media(n1, n2, n3, n4, peso_1, peso_2, peso_3, peso_4):
    calculo = ((n1 * peso_1) + (n2 * peso_2) + (n3 * peso_3) + (n4 * peso_4)) / (peso_1 + peso_2 + peso_3 + peso_4)
    return calculo


main()