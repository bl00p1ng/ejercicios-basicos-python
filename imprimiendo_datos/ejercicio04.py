def run():
    # Ejercicio 4
    # Igual que el programa anterior, pero esta vez la pirámide estará hueca (se
    # debe ver únicamente el contorno hecho con asteriscos).

    i = 1
    j = 9
    spaces = [0, 1, 3, 5, 7]
    space_aux = 0
    pyramid_base = '*'

    while i <= 9:
        if i == 1 or i == 9:
            print((' ' * int((j / 2))) + pyramid_base * i)
        else:
            print((' ' * int((j / 2))) + pyramid_base + ' ' * spaces[space_aux] + pyramid_base)
        i += 2
        j -= 2
        space_aux += 1


if __name__ == '__main__':
    run()
