def run():
    # Ejercicio 2
    # Escribe un programa que muestre tu horario de clase. Puedes usar espacios o
    # tabuladores para alinear el texto

    schedule = [
        ['🕐 Hora ', '👨‍🏫 Clase            '],
        ['08:30 am', 'Fundamentos de Python'],
        ['10:30 am', 'Matemáticas          '],
        ['12:30 pm', 'Almorzar             '],
        ['01:30 pm', 'Estadística          '],
        ['03:30 pm', 'Estructuras de datos '],
        ['04:30 pm', 'Bases de datos       ']
    ]

    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            print("| {0} ".format(schedule[i][j]), sep=',', end='')
        print('|')


if __name__ == '__main__':
    run()
