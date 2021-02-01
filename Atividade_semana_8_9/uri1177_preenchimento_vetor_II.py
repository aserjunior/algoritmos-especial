def main():
    N = [''] * 1000
    T = int(input('Insira um valor: '))
    J = 0
    Z = 0
    
    
    if T >= 2 and T <= 50:
        for i in range(len(N)):
            N[i] = J
            J += 1
            if J == T:
                J = Z
        
    
    for J in range(len(N)):
        print(f'N[{J}] = ', N[J])
        
    
main()