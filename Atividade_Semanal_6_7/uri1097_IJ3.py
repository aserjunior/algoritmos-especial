def main():
    i = 1
    J = 7
    J_salvo = 7
    contador = 0
    contador_salvo = 0
    
    
    while i <= 10:
        print(f'I={i} J={J}')
        J -= 1
        contador += 1
        if contador == 3:
            contador = 0
            novo_J = J_salvo + 2
            J = novo_J
            i = i + 2
            J_salvo = novo_J
            

main()