ejecutar_programa = True

while ejecutar_programa:
    cant_pikachu = 0
    cant_otaku = 0
    cant_pulpo = 0
    cant_anguila = 0
    
    PRECIO_PIKACHU = 4500
    PRECIO_OTAKU = 5000
    PRECIO_PULPO = 5200
    PRECIO_ANGUILA = 4800
    
    tomando_pedido = True
    print()
    print("--- BIENVENIDO AL DELIVERY DE SUSHI ---")
    
    while tomando_pedido:
        print()
        print("*** MENÚ DE PRODUCTOS ***")
        print("1. Pikachu Roll - $4500")
        print("2. Otaku Roll - $5000")
        print("3. Pulpo Venenoso Roll - $5200")
        print("4. Anguila Eléctrica Roll - $4800")
        print("5. Terminar mi pedido")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            cant_pikachu = cant_pikachu + 1
            print("¡Pikachu Roll agregado!")
        elif opcion == "2":
            cant_otaku = cant_otaku + 1
            print("¡Otaku Roll agregado!")
        elif opcion == "3":
            cant_pulpo = cant_pulpo + 1
            print("¡Pulpo Venenoso Roll agregado!")
        elif opcion == "4":
            cant_anguila = cant_anguila + 1
            print("¡Anguila Eléctrica Roll agregado!")
        elif opcion == "5":
            tomando_pedido = False
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

    total_productos = cant_pikachu + cant_otaku + cant_pulpo + cant_anguila
    subtotal = (cant_pikachu * PRECIO_PIKACHU) + (cant_otaku * PRECIO_OTAKU) + (cant_pulpo * PRECIO_PULPO) + (cant_anguila * PRECIO_ANGUILA)
    
    descuento = 0
    
    # Sección del código de descuento corregida sin bucles infinitos
    print()
    tiene_codigo = input("¿Posee un código de descuento? (si/no): ")
    
    if tiene_codigo == "si" or tiene_codigo == "SI" or tiene_codigo == "Si":
        codigo = input("Ingrese el código de descuento: ")
        
        if codigo == "soyotaku":
            descuento = int(subtotal * 0.10)
            print("¡Código aplicado con éxito! 10% de descuento.")
        else:
            print("Código no válido.")
            # Si se equivoca, la pauta pide dar la opción de volver con X o continuar 
            opcion_error = input("Presione 'X' para reingresar el código o cualquier otra tecla para continuar sin código: ")
            if opcion_error == "X" or opcion_error == "x":
                codigo = input("Ingrese el código de descuento nuevamente: ")
                if codigo == "soyotaku":
                    descuento = int(subtotal * 0.10)
                    print("¡Código aplicado con éxito!")
                else:
                    print("Código no válido. Se continuará con el pedido original.")

    total_pagar = subtotal - descuento

    print()
    print("******************************")
    print("TOTAL PRODUCTOS:", total_productos)
    print("******************************")
    print("Pikachu Roll:", cant_pikachu)
    print("Otaku Roll:", cant_otaku)
    print("Pulpo Venenoso Roll:", cant_pulpo)
    print("Anguila Eléctrica Roll:", cant_anguila)
    print("******************************")
    print("Subtotal por pagar: $", subtotal)
    print("Descuento por código: $", descuento)
    print("TOTAL: $", total_pagar)
    print("******************************")

    preguntar_salida = True
    while preguntar_salida:
        print()
        otra_compra = input("¿Desea realizar otro pedido? (si/no): ")
        if otra_compra == "no" or otra_compra == "NO" or otra_compra == "No":
            print()
            print("¡Gracias por su compra! Programa finalizado.")
            ejecutar_programa = False
            preguntar_salida = False
        elif otra_compra == "si" or otra_compra == "SI" or otra_compra == "Si":
            preguntar_salida = False
        else:
            print("Opción inválida. Responda 'si' o 'no'.")