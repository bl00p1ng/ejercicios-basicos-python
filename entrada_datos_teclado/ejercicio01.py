def run():
    # Ejercicio 1
    # Realiza un programa que pida dos números y que luego muestre el resultado
    # de su multiplicación.

    print('**** Multiplicar números ****')
    number1 = int(input(':: Escribe el multiplicando: '))
    number2 = int(input(':: Escribe el multiplicador: '))

    print(f'El resultado de multiplicar {number1} * {number2} es {number1 * number2}')


if __name__ == '__main__':
    run()