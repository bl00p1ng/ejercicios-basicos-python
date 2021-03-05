def run():
    # Ejercicio 7
    # Realiza un conversor de Kb a Mb

    print('**** CONVERSOR DE KILOBYTES A MEGABYTES')
    kb_to_mb = int(input(':: Escribe la cantidad de Kilobytes que quieres convertir: '))

    print(f'{kb_to_mb} Kb equivalen a {kb_to_mb / 1024} Mb')


if __name__ == '__main__':
    run()
