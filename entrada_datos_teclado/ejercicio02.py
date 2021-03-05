def run():
    # Ejercicio 2
    # Escribe un programa que sume, reste, multiplique y divida dos números
    # introducidos por teclado.

    print('**** Operaciones básicas ****')
    number1 = int(input(':: Escribe un número: '))
    number2 = int(input(':: Escribe otro número: '))

    print(f'El resultado de {number1} + {number2} es {number1 + number2}')
    print(f'EL resultado de {number1} - {number2} es {number1 - number2}')
    print(f'EL resultado de {number1} x {number2} es {number1 * number2}')
    print(f'EL resultado de {number1} ➗ {number2} es {number1 //number2}')


if __name__ == '__main__':
    run()
