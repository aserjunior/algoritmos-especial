def main():
    P = [''] * 5
    I = [''] * 5
    contador_p = 0
    contador_i = 0
    contador = 0
    max = 15
    resto_i = 0
    resto_p = 0


    while contador < max:
        valor = int(input('Insira um valor: '))
        if valor % 2 == 0:
            P[contador_p] = valor
            contador_p += 1
            if contador_p == 5:
                for i in range(len(P)):
                    print(f'par[{i}] = ', P[i])
                    contador_p = 0
        
        
        elif (valor + 1) % 2 == 0:
            I[contador_i] = valor
            contador_i += 1
            if contador_i == 5:
                for i in range(len(I)):
                    print(f'impar[{i}] = ', I[i])
                    contador_i = 0
     
        contador += 1


    while resto_i < contador_i:
        print(f'impar[{resto_i}] = ', I[resto_i])
        resto_i += 1
    while resto_p < contador_p:
        print(f'par[{resto_p}] = ', P[resto_p])
        resto_p += 1
    
    
main()
