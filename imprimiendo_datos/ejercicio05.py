def run():
    # Ejercicio 5
    # Igual que el programa anterior, pero esta vez la pirámide debe aparecer
    # invertida, con el vértice hacia abajo.

    i = 9  # Define el número de * que se van a imprimir en cada iteración

    # j → Define la separación de cada fila de * con respeto al borde de la pantalla.
    # Esto permite darle a la figura el efecto de pirámide
    j = 1

    # spaces → Establece la separación entre el * izquierdo y el derecho en cada iteración.
    # Permite crear el efecto de "pirámide hueca"
    spaces = [0, 5, 3, 1, 0]

    space_aux = 0  # indice para iterar la lista spaces
    pyramid_base = '*'

    while i > 0:
        # Imprime la base (i == 9) y el vértice (i == 1) de la pirámide
        if i == 1 or i == 9:
            print((' ' * int((j / 2))) + pyramid_base * i)
        # Imprime la parte hueca de la pirámide.
        # (' ' * int((j / 2))) → Calcula la separación de la fila con respecto al borde de la pantalla
        # ' ' * spaces[space_aux] → Calcula el "vacío" dentro de la pirámide
        else:
            print((' ' * int((j / 2))) + pyramid_base + ' ' * spaces[space_aux] + pyramid_base)
        i -= 2
        j += 2
        space_aux += 1


if __name__ == '__main__':
    run()
