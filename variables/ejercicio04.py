def run():
    # Ejercicio 4
    # Realiza un conversor de euros a dólar. La cantidad en euros que se quiere
    # convertir deberá estar almacenada en una variable.

    eur_in_usd = 1.21

    print('💱 Conversor de Euros a Dólares')
    user_eur = float(input(':: Ingresa la cantidad de Euros que quieres  convertir: '))

    eur_converted = user_eur * eur_in_usd
    print('€' + str(user_eur) + ' 💶 Euros equivalen a $' + str(eur_converted) + ' 💵 Dólares')


if __name__ == '__main__':
    run()
