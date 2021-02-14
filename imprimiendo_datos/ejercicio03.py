def run():
    # Ejercicio 3
    # Escribe un programa que pinte por pantalla una pirámide rellena a base de
    # asteriscos. La base de la pirámide debe estar formada por 9 asteriscos.

    i = 1
    j = 9
    pyramid_base = '*'

    while i <= 9:
        print((' ' * int((j / 2))) + pyramid_base * i)
        i += 2
        j -= 2


if __name__ == '__main__':
    run()
