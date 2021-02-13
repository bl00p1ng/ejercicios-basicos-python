def run():
    # Ejercicio 6
    # Escribe un programa que calcule el total de una factura a partir de la base
    # imponible (precio sin IVA). La base imponible estará almacenada en una
    # variable.

    print('💰 Calcula el total de una factura a partir de la base imponible (precio sin IVA)')
    taxable_base = float(input(':: Ingresa el precio---- sin IVA: '))

    iva = 1.19
    total = round(taxable_base * iva)

    print('El total de la fractura es : $' + str(total))


if __name__ == '__main__':
    run()
