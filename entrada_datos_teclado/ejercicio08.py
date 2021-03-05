def calculate_final_price(taxable_base, iva, promo_code):
    print(f'➡ IVA ({iva * 100}%): {taxable_base - (taxable_base - (taxable_base * iva))}')

    price_with_iva = taxable_base + (taxable_base * iva)
    print(f'➡ Precio con IVA: {price_with_iva}')

    if promo_code == 'nopro':
        print(f'➡ Cód. promo. ({promo_code}): No hay descuento')
        print(f'➡ TOTAL: {price_with_iva}')

    elif promo_code == 'mitad':
        total = price_with_iva / 2

        print(f'➡ Cód. promo. ({promo_code}): -${price_with_iva / 2}')
        print(f'➡ TOTAL: ${total}')

    elif promo_code == '5porc':
        total = price_with_iva - (price_with_iva * 0.05)

        print(f'➡ Cód. promo. ({promo_code}): -${round(price_with_iva - total, 2)}')
        print(f'➡ TOTAL: ${round(total, 2)}')
    else:
        print('⚠ Elegiste un Código Promocional incorrecto')


def run():
    # Ejercicio 12
    # Escribe un programa que calcule el precio final de un producto según su
    # base imponible (precio antes de impuestos), el tipo de IVA aplicado (general,
    # reducido o super reducido) y el código promocional. Los tipos de IVA general,
    # reducido y super reducido son del 21%, 10% y 4% respectivamente. Los códigos promocionales
    # pueden ser nopro, mitad, meno5 o 5porc que significan
    # respectivamente que no se aplica promoción, el precio se reduce a la mitad,
    # se descuentan 5 euros o se descuenta el 5%. El ejercicio se da por bueno si se
    # muestran los valores correctos, aunque los números no estén tabulados

    print('**** CALCULA EL PRECIO FINAL DE UN PRODUCTO ****')
    taxable_base = int(input(':: Introduzca la base imponible: '))
    iva_type = str.lower(input(':: Introduzca el tipo de IVA (general, reducido o superreducido): '))
    promo_code = str.lower(input(':: Introduzca el código promocional (nopro, mitad, meno5 o 5porc): '))

    print(f'➡ Base imponible: {taxable_base}')

    if iva_type == 'general':
        calculate_final_price(taxable_base, 0.21, promo_code)
    elif iva_type == 'reducido':
        calculate_final_price(taxable_base, 0.1, promo_code)
    elif iva_type == 'superreducido':
        calculate_final_price(taxable_base, 0.04, promo_code)
    else:
        print(f'⚠ {iva_type} NO es un tipo de IVA válido\nLos valores válidos son: general, reducido o superreducido')


if __name__ == '__main__':
    run()
