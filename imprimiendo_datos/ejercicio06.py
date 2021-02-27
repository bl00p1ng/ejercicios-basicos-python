import random

houses_number = 0
enable_animals = 2


def generate_drawing(houses_number):
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

    houses = [
    """
                     x
          .-. _______|
          |=|/     /  \\
          | |_____|_""_|
          |_|_[X]_|____|
    """,
    """
       +
       A_
      /\-\\
     _||"|_
    ~^~^~^~^
    """,
    """
      ____||____
     ///////////\\
    ///////////  \\
    |    _    |  |
    |[] | | []|[]|
    |   | |   |  |
    """,
    """
        .-. ,-.
    '   (%%'`.               __
     `-(%|%)% )             /()\````\\
       (%\K /,             /____\____\\
        %.\V/%.)           |n  n|.___|
       (%\%`(',            | __ /_\___\\
         %| ,)   ____      | || |n|n_n|
          | |  /____ "_     / |
          | |_" .-. "_ "__,'  /
         ,| |  |,' |  "__,...'  
    """,
    """
                `'::.
    _________H ,%%&%,
   /\     _   \%&&%%&%
  /  \___/^\___\%&%%&&
  |  | []   [] |%\Y&%'
  |  |   .-.   | ||  
  @._|@@_|||_@@|~||
     `'''') )''''`
    """,
    """
          `'::::.
        _____A_
       /      /\\
    __/__/\__/  \___
   /__|" '' "| /___/\\
   |''|"'||'"| |' '||
   `**`**))*`*`****
    """,
    """
                                +&-
                          _.-^-._    .--.
                       .-'   _   '-. |__|
                      /     |_|     \|  |
                     /               \  |
                    /|     _____     |\ |
                     |    |==|==|    |  |
 |---|---|---|---|---|    |--|--|    |  |
 |---|---|---|---|---|    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    ]

    animals = [
    """
             (__)    
     `\------(oo)
       ||    (__)
       ||w--||     \|/
    """,
    """
       _ ____
     /( ) _   \\
    / //   /\` \,  ||--||--||-
      \|   |/  \|  ||--||--||-
~^~^~^~~^~~~^~~^^~^^^^^^^^^^^^
    """,
    """
        ,--,
  _ ___/ /\|
 ;( )__, )
; //   '--;
  \     |
   ^    ^
    """,
    """
         .
 ..^____/
`-. ___ )
  ||  || 
    """,
    """
        __
   (___()'`;
   /,    /`
   \\\\"--\\\\
    """
    ]

    # Generar Sol
    sun = ''
    sun += (suns[random.randint(0, 3)])
    print(sun)

    # Generar paisaje
    landscape = []

    for i in range(houses_number):
        landscape += (houses[random.randint(0, 6)])
    print(landscape)


def run():
    # Ejercicio 6
    # Escribe un programa que pinte por pantalla alguna escena - el campo, la
    # habitación de una casa, un aula, etc. - o algún objeto animado o inanimado
    # - un coche, un gato, una taza de café, etc. Ten en cuenta que puedes utilizar
    # caracteres como *, +, <, #, @, etc.

    print('✍ GENERADOR DE ASCII ART')
    print('🏞 Crea una escena campestre personalizada 🌄')

    # Configurar dibujo
    houses_number = int(input(':: Escribe el número de casas que quieres en la escena: '))
    #enable_animals = int(input(':: Quires ver animales en tu dibujo \n(1 = SI | 2 = NO): '))

    # Crear dibujo
    generate_drawing(houses_number)


if __name__ == '__main__':
    run()
