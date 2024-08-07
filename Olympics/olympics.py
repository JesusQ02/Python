print("SIMULADOR DE JUEGOS OLIMPICOS")

while True:

    print ()
    print ("1. Registro de eventos deportivos.")
    print ("2. Registro de participantes.")
    print ("3. Simulacion de eventos.")
    print ("4. Creacion de informes.")
    print ("5. Salir.")

    option = input ("Seleccione una accion: ")

    match option:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            print ("Saliendo del simulador...")
            break
        case _:
            print ("Opcion invalida. Por favor selecciona una opcion valida")
