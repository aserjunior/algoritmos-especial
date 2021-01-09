def main():
    #entrada
    idade = int(input("Dias: "))


    #processamento
    anos = idade // 365
    resto = idade % 365
    meses = resto // 30
    dias = resto % 30


    #saída
    print(f"{anos} ano(s)")
    print(f"{meses} mes(es)")
    print(f"{dias} dia(s)")


main()