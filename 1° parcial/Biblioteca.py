#Gestion de biblioteca

titulos = ["Cien años de soledad", "1984","La odisea"]
ejemplares = [4,6,2]

opcion = 0

while opcion != 8:
    print("\n--- menu Biblioteca ---")
    print("1. ingresar titulos")
    print("2. ingresar ejemplares")
    print("3. mostrar catalogo")
    print("4. consultar disponibilidad")
    print("5. listar agotados")
    print("6. agregar titulo")
    print("7. actualizar ejemplares")
    print("8. salir")

    entrada = input("seleccione una opcion (1-8): ")

    #validacion

    if not entrada.isdigit():  
        print("debe ingresar un numero del 1 al 8:")
        continue             

    opcion = int(entrada)

    opcion = int(entrada)

    match opcion:
        case 1: #ingresar titulos
            cantidad = input("¿cuantos titulos desea agregar?")
            if cantidad.isdigit():
                for _ in range(int(cantidad)):
                    titulo = input("ingrese el titulo:")
                    titulos.append(titulo)
                    ejemplares.append(0)
            else:
                print("numero invalido")

        case 2: #ejemplares
            for i in range(len(titulos)):
                cantidad = input (f"ejemplares de '{titulos[i]}':")
                if cantidad.isdigit():
                    ejemplares[i] = int(cantidad)
                else:
                    print("numero invalido, se mantiene el valor anterior")

        case 3: #catalogo
            print("\n--- catalogo ---")
            for i in range(len(titulos)):
                print(f"'{titulos[i]}' - {ejemplares[i]} ejemplares  ")
    
        case 4: #disponibilidad
            buscar = input("titulo a buscar:").lower()
            encontrado = False
            for i in range(len(titulos)):
                if titulos[i].lower() == buscar:
                    print(f"'{titulos[i]}' tiene {ejemplares[i]} ejemplares")
                    encontrado = True
                    break
            if not encontrado:
                    print("titulo no encontrado")
    
        case 5: #agotados
            print("\n--- agotados ---")
            agotados = False
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(titulos[i])
                    agotados = True
            if not agotados:
                    print("no hay libros agotados")

        case 6: #titulos
            titulo = input("ingrese nuevo titulo:")
            titulos.append(titulo)
            ejemplares.append(0)
            print(f"'{titulo}' agregado con 0 ejemplares.")    

        case 7: #ejemplares
            buscar = input ("titulos a actualizar:").lower()
            encontrado = False
            for i in range(len(titulos)):
                if titulos[i].lower() == buscar:
                    cambio = input  ("cantidad a sumar(devolucion) o restar(prestamo):")
                    if cambio.lstrip('-').isdigit():
                        ejemplares[i] += int(cambio)
                        if ejemplares[i] < 0:
                            ejemplares[i] = 0
                        print(f"nuevo stock de {titulos[i]}: {ejemplares[i]}")
                    encontrado = True
                    break
                if not encontrado:
                    print("titulo no encontrado")

        case 8:
            print("saliendo...")

        case _:
            print("opcion invalida. Ingrese un numero del 1 al 8")
    