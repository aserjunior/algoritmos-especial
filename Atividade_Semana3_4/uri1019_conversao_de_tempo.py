def main():
    #entrada
    N = int(input("Segundos: "))


    #processamento
    horas = N // 3600
    resto = N % 3600
    minutos = resto // 60
    segundos = resto % 60


    #saída
    print(f"{horas} : {minutos} : {segundos}")


main()