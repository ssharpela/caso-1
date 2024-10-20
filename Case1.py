def calcular_precio():
    descuentos = {
        101: 0.20,  # Bisutería - 20% de descuento
        205: 0.35,  # Calzado - 35% de descuento
        105: 0.10,  # Lencería - 10% de descuento
        301: 0.50  # Abrigos - 50% de descuento
    }

    # Entrada de datos
    articulo = input("Nombre del artículo: ")
    cantidad = int(input("Cantidad comprada: "))
    precio_unitario = float(input("Precio unitario: ₡"))
    codigo_categoria = int(input("Código de la categoría del artículo: "))

    # Verificar si el código de categoría tiene un descuento
    if codigo_categoria in descuentos:
        porcentaje_descuento = descuentos[codigo_categoria]
        descuento_aplicado = porcentaje_descuento * 100  # Convertir a porcentaje
    else:
        porcentaje_descuento = 0
        descuento_aplicado = 0

    # Cálculos
    subtotal = cantidad * precio_unitario
    descuento = subtotal * porcentaje_descuento
    subtotal_con_descuento = subtotal - descuento
    impuesto = subtotal_con_descuento * 0.13
    total = subtotal_con_descuento + impuesto

    # Detalle de la compra
    print("\n--- Detalle de la compra ---")

    # Imprimir tabla de productos
    print(f"{'Código':<10}{'Nombre de Producto':<25}{'Cant.':<15}{'Precio Unitario':<15}")
    print('-' * 65)
    print(f"{codigo_categoria:<10}{articulo:<25}{cantidad:<15}₡{precio_unitario:.2f}")

    # Imprimir resumen de precios
    print('=' * 65)
    print(f"{'Subtotal:':<50} ₡{subtotal:.2f}")
    print(f"{'(menos) Descuento aplicado (' + str(descuento_aplicado) + '%):':<50} ₡{descuento:.2f}")
    print('-' * 65)
    print(f"{'Subtotal con descuento:':<50} ₡{subtotal_con_descuento:.2f}")
    print(f"{'Impuesto (13%):':<50} ₡{impuesto:.2f}")
    print(f"{'Total a pagar:':<50} ₡{total:.2f}")


# Llamada a la función
calcular_precio()
