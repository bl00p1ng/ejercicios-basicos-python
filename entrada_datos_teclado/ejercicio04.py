def run():
    # Ejercicio 4
    # Escribe un programa que calcule el área de un triángulo.

    print('**** Área de un triángulo ****')
    width = int(input(':: Escribe la base del triángulo: '))
    height = int(input(':: Escribe la altura del triángulo: '))

    print(f'El área del triángulo es {(width * height) / 2}')


if __name__ == '__main__':
    run()
