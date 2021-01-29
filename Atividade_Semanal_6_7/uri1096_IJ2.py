def main():
    i = 1
    J = 7


    while J >= 5:
        print(f'I={i} J={J}')
        J -= 1
        if J == 4:
            i = i + 1
            J = 7
            if i == 10:
                break


main()