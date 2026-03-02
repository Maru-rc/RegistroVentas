nombre_cliente = input("Ingresa tu nombre: ")
cliente_vip = input("Eres cliente vip? (si/no): ").lower()
productos = ""
cantidad_productos = int(input("Cuantos productos quieres ingresar?: "))
subtotal = 0
descuento_vip = 0.10
for i in range(cantidad_productos):
    nombre = input("\nIngresa el nombre del producto: ")
    precio = input("Ingresa el precio del producto: ")
    productos += f"\n{nombre} - ${precio}"
    subtotal += int(precio)


iva = subtotal*0.19
descuento_vip = subtotal*0.10
subtotal_iva = subtotal + iva
subtotal_vip_iva = subtotal + iva - descuento_vip if cliente_vip == "si" else 0
print(
    f"""
--------------------------------------------------------
              Bienvenido {nombre_cliente}
--------------------------------------------------------
Producto/Precio
{productos}
--------------------------------------------------------
              Precio a pagar
--------------------------------------------------------
Subtotal: ${subtotal}
Iva 19%: ${round(iva)}
subtotal + iva: ${round(subtotal+iva)}
    """

    ),print(f"Subtotal con descuento vip: ${subtotal-descuento_vip}" if cliente_vip == "si" else "" )
print(f"Total: ${round(subtotal_vip_iva)}" if cliente_vip =="si" else f"Total: {subtotal_iva}")