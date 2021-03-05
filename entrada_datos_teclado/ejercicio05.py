def run():
    # Ejercicio 5
    # Escribe un programa que calcule el salario semanal de un empleado en base
    # a las horas trabajadas, a razón de 12 euros la hora

    print('**** CALCULADORA DE SALARIO ****')
    hours = int(input(':: Ingresa el número de horas que trabajaste esta semana: '))

    print(f'Trabajaste {hours} horas. Tu salario para esta semana es de ${hours * 12} EUR')


if __name__ == '__main__':
    run()
