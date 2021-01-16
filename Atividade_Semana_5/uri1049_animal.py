def main():
    A = str(input('Insira a primeira palavra: '))
    B = str(input('Insira a segunda palavra: '))
    C = str(input('Insira a terceira palavra: '))


    if A == 'vertebrado':
        B == 'ave' or B == 'mamifero'
        if B == 'ave':
            C == 'carnivoro' or 'onivoro'
            if C == 'carnivoro':
                print('aguia')
            elif C == 'onivoro':
                print('pombo')
        elif B == 'mamifero':
            C == 'onivoro' or 'herbivoro'
            if C == 'onivoro':
                print('homem')
            elif C == 'herbivoro':
                print('vaca')
    elif A == 'invertebrado':
        B == 'inseto' or B == 'anelideo'
        if B == 'inseto':
            C == 'hematofogo' or C == 'herbivoro'
            if C == 'hematofogo':
                print('pulga')
            elif C == 'herbivoro':
                print('lagarta')
        elif B == 'anelideo':
            C == 'hematofogo' or C == 'onivoro'
            if C == 'hematofogo':
                print('sanguessuga')
            elif C == 'onivoro':
                print('minhoca')


main()