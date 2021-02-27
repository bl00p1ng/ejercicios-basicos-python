def run():
    # Ejercicio 5
    # Realiza un conversor de dólar a euros. La cantidad en pesetas que se quiere
    # convertir deberá estar almacenada en una variable.

    usd_in_eur = 0.82

    print('💱 Conversor de Dólares a Euros')
    user_usd = float(input(':: Ingresa la cantidad de Dólares que quieres convertir: '))

    usd_converted = user_usd * usd_in_eur

    print('$' + str(user_usd) + ' Dólares equivalen a €' + str(usd_converted))


if __name__ == '__main__':
    run()
