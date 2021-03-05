def run():
    # Ejercicio 06
    # Realiza un conversor de Mb a Kb.

    print('**** CONVERSOR DE MEGABYTES A KILOBYTES ****')
    mb_to_kb = int(input(':: Escribe la cantidad de Megabytes que quieres convertir: '))

    print(f'{mb_to_kb} Mb equivalen a {mb_to_kb * 1024} Kb')


if __name__ == '__main__':
    run()
