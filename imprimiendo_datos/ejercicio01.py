def show_matrix(matrix):
    # Imprimir valores de la Matriz
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("| {0} ".format(matrix[i][j]), sep=',', end='')
        print('|')


def run():
    # Ejercicio 1
    # Escribe un programa que muestre por pantalla 10 palabras en inglés junto
    # a su correspondiente traducción al español. Las palabras deben estar
    # distribuidas en dos columnas y alineadas a la izquierda. Pista: Se puede
    # insertar un tabulador mediante \t.

    words = [
        ['Computer', 'Computador'],
        ['Network', 'Red'],
        ['Data', 'Datos'],
        ['Programming', 'Programación'],
        ['Developer', 'Desarrollador'],
        ['Keyboard', 'Teclado'],
        ['Data Science', 'Ciencia de Datos'],
        ['Scientist', 'Científico'],
        ['Analyst', 'Analista'],
        ['Server', 'Servidor'],
    ]

    show_matrix(words)


if __name__ == '__main__':
    run()
