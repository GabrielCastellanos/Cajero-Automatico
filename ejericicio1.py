# Simulación de un cajero automático 
# Variables iniciales de billetes en el inventario del cajero.
# Se utiliza un diccionario para facilitar la gestión del inventario.
inventario = {
    1000: 10,
    500: 10,
    200: 10,
    100: 10,
    50: 10
}

# Se inicia el cajero automático
print("\n--- Cajero Automático ---")
print("Inventario inicial de billetes:")
for denominacion, cantidad in inventario.items(): # Muestra el inventario inicial
    print(f"  - ${denominacion}: {cantidad} billetes")

# El bucle principal del programa
while True:
    try:
        # Se pide el monto a retirar al usuario
        entrada = input("\nIngrese el monto a retirar (0 para salir): ")
        monto = int(entrada)

        # Si el monto es 0, se sale del programa
        if monto == 0:
            print("\nGracias por usar el cajero automático. ¡Hasta pronto!")
            break

        # Validaciones del monto
        if monto < 0:
            print("El monto no puede ser negativo. Por favor, ingrese un valor válido.")
            continue
            
        if monto % 50 != 0:
            print("El monto debe ser un múltiplo de 50.")
            continue
        
        # Variables de billetes a entregar para esta transacción.
        # Se crea un diccionario temporal para no modificar el inventario real hasta que la transacción sea exitosa.
        entregar = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0}
        
        monto_restante = monto
        
        # Lógica para dispensar los billetes (donde se busca minimizar la cantidad de billetes entregados)
        # Se itera sobre las denominaciones de mayor a menor
        denominaciones = sorted(list(inventario.keys()), reverse=True)
        
        for denominacion in denominaciones:
            if monto_restante >= denominacion:
                # Se calcula cuántos billetes de esta denominación se necesitan
                cantidad_necesaria = monto_restante // denominacion
                
                # Se verifica si hay suficientes billetes en el inventario
                cantidad_a_dar = min(cantidad_necesaria, inventario[denominacion])
                
                if cantidad_a_dar > 0:
                    entregar[denominacion] = cantidad_a_dar
                    monto_restante -= cantidad_a_dar * denominacion
        
        # Se verifica si el monto restante es 0
        if monto_restante == 0:
            print("\nTransacción exitosa. Se le entregará:")
            # Se muestra el detalle de los billetes entregados y se actualiza el inventario
            for denominacion, cantidad in entregar.items():
                if cantidad > 0:
                    print(f"  - {cantidad} billetes de ${denominacion}")
                    inventario[denominacion] -= cantidad
            
            print("\n--- Nuevo inventario de billetes ---")
            for denominacion, cantidad in inventario.items():
                print(f"  - ${denominacion}: {cantidad} billetes")

        else:
            print("\nLo sentimos, no es posible entregar esa cantidad con los billetes disponibles en el cajero.")
            
    except ValueError:
        # Manejo de error si el usuario ingresa algo que no es un número
        print("Entrada no válida. Por favor, ingrese un número entero.")
