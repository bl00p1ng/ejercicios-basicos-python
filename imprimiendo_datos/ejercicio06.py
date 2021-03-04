import random


def choose_random_option(elements_list):
    """
    Elige una opción aleatoria entre los elementos de una lista.
    Es una función auxiliar de generate_scene()

    :param elements_list: Lista con los elementos a elegir
    :return: Elemento elegido aleatoriamente
    """
    option_chosen = (elements_list[random.randint(0, len(elements_list) - 1)])
    return option_chosen


def generate_scene(time):
    """
    Genera una escena campestre con ASCII Art. Dicha escena puede ser diurna o nocturna

    :param time: Establece el momento del día en la escena (1 == día/ 2 == noche)
    :return: Escena campestre terminada
    """
    suns = [
        """
        |
      \ | /
       \*/
    --**O**-- 
       /*\\
      / | \\
        |
        """,
        """
            .
          \ | /
        '-.;;;.-'
       -==;;;;;==-
        .-';;;'-.
          / | \\
            '
        """,
        """
               |
         \     |     /
           \       /
             ,d8b,           .,
     (')-")_ 88888 ---   ;';'  ';'.
    ('-  (. ')98P'      ';.,;    ,;
     '-.(. ')'     \       '.';.'
               |    \\
               |
        """,
        """
              ;   :   ;
       .   \_,!,_/   ,
        `.,'     `.,'
         /         \\
    ~ -- :         : -- ~
         \         /
        ,'`._   _.'`.
       '   / `!` \   `
          ;   :   ;  
        """
    ]

    moons = [
        """
          _.._
        .' .-'`
       /  /
       |  |
       \\  '.___.;
        '._  _.'
        """,
        """
         _.._
       .' .-'`
      /  /
      |  |
      \  \\
       '._'-._
          ```

        """,
        """
       _..._     
     .:::::::.    
    :::::::::::   
    ::::::::::: 
    `:::::::::'  
      `':::'' 
        """,
        """
            
    *  --.
        \  \   *
         )^ |    *
*       <_, |
   *    ./ /
       --'   *
        """
    ]

    houses = [
    """
                                                                 `'::.
                                                           _________H ,%%&%,
                                        ____||____        /\     _   \%&&%%&%
                     x        +        ///////////\\      /  \___/^\___\%&%%&&
          .-. _______|        A_      ///////////  \\     |  | []   [] |%\Y&%'         __
          |=|/     /  \\      /\-\\     |    _    |  |     |  |   .-.   | ||       (___()'`;      
          | |_____|_""_|    _||"|_    |[] | | []|[]|     @._|@@_|||_@@|~||       /,    /`
          |_|_[X]_|____|   ~^~^~^~^   |   | |   |  |       `'''') )''''`         \\\\"--\\\\
    """,

        """
        .-. ,-.                                                                                +&-
    '   (%%'`.               __                                                              _.-^-._    .--.
     `-(%|%)% )             /()\````\\                                                     .-'   _   '-. |__|
       (%\K /,             /____\____\\          `'::::.                                  /     |_|     \|  |
        %.\V/%.)           |n  n|.___|           _____A_                                /               \  |
       (%\%`(',            | __ /_\___\\        /      /\\                               /|     _____     |\ |    
         %| ,)   ____      | || |n|n_n|     __/__/\__/  \___                            |    |==|==|    |  |         (__)     
          | |  /____ "_     / |            /__|" '' "| /___/\\       |---|---|---|---|---|    |--|--|    |  |  \------(oo)    
          | |_" .-. "_ "__,'  /            |''|"'||'"| |' '||       |---|---|---|---|---|    |==|==|    |  |   ||    (__)    
         ,| |  |,' |  "__,...'             `**`**))*`*`****        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^||w--||     \|/
    """
    ]

    # Evaluar el momento del día de la escena
    if time == 1:
        # Generar Sol
        print(choose_random_option(suns))

        # Generar paisaje
        generate_landscape(houses)

    elif time == 2:
        # Generar luna
        print(choose_random_option(moons))

        # Generar paisaje
        generate_landscape(houses)

    # Verifica que el valor de time sea un número positivo y que no sea mayor a 2
    elif type(time) == int and (time > 2 or (time < 1 and time != 0)):
        print('⚠ Debes elegir una opción valida como 1 ó 2\n')
        run()


def generate_landscape(houses):
    """
    Elige un paisaje de entre los elementos de una lista con paisajes y lo imprime en pantalla.
    Es una función auxiliar de generate_scene()

    :param houses: Lista con los paisajes a elegir
    :return: Paisaje impreso en pantalla
    """
    landscape = choose_random_option(houses)
    print(landscape)


def run():
    # Ejercicio 6
    # Escribe un programa que pinte por pantalla alguna escena - el campo, la
    # habitación de una casa, un aula, etc. - o algún objeto animado o inanimado
    # - un coche, un gato, una taza de café, etc. Ten en cuenta que puedes utilizar
    # caracteres como *, +, <, #, @, etc.

    print('**** GENERADOR DE ASCII ART ****')
    print(':: Crea una escena campestre personalizada')

    day_or_night = 0  # Establece el momento del día en que se creará el dibujo.
    try:
        day_or_night = int(input(':: Quieres que la escena sea de dia o de noche?\n 1. Día\n 2. Noche \n➡ Tu elección: '))
    except ValueError as e:
        print('⚠ Elegiste una opción incorrecta\n')
        run()

    # Crear dibujo
    generate_scene(day_or_night)


if __name__ == '__main__':
    run()
