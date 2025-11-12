#importamos los modulos necesarios

import csv
import os

#nombre del archivo csv para la persistencia
#lo defino como constante, ya que no es una variable global de estado

NOMBRE_ARCHIVO = "biblioteca.csv"

# -- FUNCIONES DE UTILIDAD Y VALIDACION --

def normalizar_titulo(titulo):

#convierte a minusculas y sacamos espacios al inicio y al final

    return titulo.strip() .lower()

def buscar_libro(catalogo, titulo_buscado):

    #busca un libro en el catalogo por su titulo normalizado
    #devuelve el diccionario del libro si lo encuentra, o None si no lo hace

    titulo_normalizado = normalizar_titulo(titulo_buscado)
    for libro in catalogo:
        if normalizar_titulo(libro["TITULO"]) == titulo_normalizado:
            return libro
        return None
    
def validar_cantidad_int(mensaje_input, min_valor=0):

    #pide al usuario un numero y valida que sea entero, sigue pidiendo hasta que sea valido

    while True:
        entrada = input(mensaje_input)
        if entrada.isdigit():
            cantidad = int(entrada)
            if cantidad >= min_valor:
                return cantidad
            else:
                print(f"Error: la cantidad debe ser {min_valor} o mas")
        else:
            print(f"Error: ingrese solo numeros enteros positivos")

def validar_nuevo_titulo(catalogo, mensaje_input):

    #pide al usuario un titulo y valida que no este vacio y no exista
    #sigue pidiendo hasta que sea valido

    while True:
        titulo = input(mensaje_input)
        titulo_limpio = titulo.strip()

        if not titulo_limpio:
            print(f"Error: el titulo no puede estar vacio")
        elif buscar_libro(catalogo, titulo_limpio):
            print(f"Error: ese titulo ya existe en el catalogo")
        else:
            #devuelvo el titulo con el formato original que dio el user
            return titulo_limpio
        
#--- FUNCIONES DE PERSISTENCIA (CSV)---

def cargar_catalogo(nombre_archivo):

    #carga el catalogo desde el archivo csv, si no existe devuelve una lista vacia

    catalogo = []

    #uso os.path.exists para evitar FileNotFoundError (no uso try-except)

    if not os.path.exists(nombre_archivo):
        return catalogo
    
    with open (nombre_archivo, mode = 'r', encoding= 'utf-8', newline='') as f:
        reader = csv.DictReader(f) 
        for row in reader:
            
            #me aseguro que la cantidad cargue como entero
            if "CANTIDAD" in row and row ["CANTIDAD"].isdigit():
                row["CANTIDAD"] = int(row["CANTIDAD"])
            else:
                #si falta la cantidad o no es digito, asumimos 0
                row["CANTIDAD"] = 0
            if "TITULO" in row:
                catalogo.append(row)
    
    print(f"catalogo cargado exitosamente desde CSV.")
    return catalogo

def guardar_catalogo(nombre_archivo, catalogo):

    #guarda el estado actual del catalogo en el CSV, sobreescribe por completo
    
    fieldnames = ["TITULO", "CANTIDAD"]

    with open (nombre_archivo, mode = 'w', encoding= 'utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(catalogo)

    print("\n[Operacion exitosa: El catalogo ha sido guardado en el CSV.]")

    #--- FUNCIONES DEL MENU (LOGICA) ---

def ingresar_multiples_titulos(catalogo):

        #funcionalidad 1: permite ingresar varios libros a la vez
        #devuelve el catalogo modificado

    print("\n--- 1. Ingresar titulos (Multiples) ---")
    num_libros = validar_cantidad_int("¿Cuantos libros desea cargar?", min_valor=1)

    agregados = 0
    for i in range(num_libros):
        print(f"\nLibro {i+1} de {num_libros}")
        titulo = validar_nuevo_titulo(catalogo, "Titulo:")
        cantidad = validar_cantidad_int("cantidad inicial (>=0):", min_valor=0)

        catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
        agregados += 1
        print(f"'{titulo}' agregado")

        if agregados > 0:
            print(f"\nSe agregaron {agregados} nuevos titulos")
        else:
            print("No se agregaron titulos")

        return catalogo

def ingresar_ejemplares(catalogo):

        #Funcionalidad 2: sumamos ejemplares a un titulo existente
        # devuelve el catalogo modificado

    print("\n--- 2. Ingresar ejemplares (Sumar stock) ---")
    if not catalogo:
        print("El catalogo esta vacio. No se pueden agregar ejemplares")
        return catalogo

    titulo_buscado = input("Titulo del libro al que desea sumar ejemplares:")        
    libro = buscar_libro(catalogo, titulo_buscado)

    if libro:
        cantidad_a_sumar = validar_cantidad_int(f"¿Cuantos ejemplares de'{libro['TITULO']}' desea agregar?")
        libro["CANTIDAD"] += cantidad_a_sumar
        print(f"Stock actualizado. Nueva cantidad: {libro['CANTIDAD']}")
    else:
        print("Error: titulo no encontrado")

    return catalogo

def mostrar_catalogo(catalogo):

    #Funcionalidad 3: Mostramos todos los libros y su stock

    print("\n--- 3. Catalogo completo ---")
    if not catalogo:
        print("El catalogo esta vacio")
    else:
        print(f"Total de titulos: {len(catalogo)}")
        print("-" * 30)
        for libro in catalogo:

         print(f" Titulo: {libro['TITULO']}")
         print(f"stock: {libro['CANTIDAD']} ejemplares")
         print("-" * 30)

def consultar_disponibilidad(catalogo):

    #Funcionalidad 4: busca un titulo y mostramos su stock

    print("\n--- 4. Consultar disponibilidad ---")
    if not catalogo:
        print("El catalogo esta vacio")
        return
    
    titulo_buscado = input("Titulo del libro que desea consultar:")
    libro = buscar_libro(catalogo, titulo_buscado)

    if libro:
        print(f"Disponibilidad de '{libro['TITULO']}': {libro['CANTIDAD']}' ejemplares")
    else:
        print("Error: titulo no encontrado")

def listar_agotados(catalogo):

    #Funcionalidad 5: muestra los libros con cantidad == 0 

    print("\n --- 5. Listar titulos agotados ---")

    #Creo una lista temporal con los agotados
    agotados = []
    for libro in catalogo:
        if libro ["CANTIDAD"] == 0:
            agotados.append(libro)

    if not agotados:
        print("No hay libros agotados")
    else:
        print(f"Se encontraron {len(agotados)} titulos agotados:")
        for libro in agotados:
            print(f" - {libro['TITULO']}")

def agregar_titulo_individual(catalogo):

    #Funcionalidad 6: alta de un slo libro (igual a func.1 pero individual)

    print("\n ---6. Agregar titulo (individual) ---")
    titulo = validar_nuevo_titulo(catalogo, "Nuevo titulo:")
    cantidad = validar_cantidad_int(" Cantidad inicial (>=0):", min_valor=0)

    catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    print(f"'{titulo}' agregado correctamente")

    return catalogo

def actualizar_prestamo_devolucion(catalogo):

    #Funcionalidad 7: Realiza un prestamo (-1) o devolucion (+1)

    print("\n--- 7. Actualizar ejemplares (Prestamo/Devolucion) ---")
    if not catalogo:
        print("El catalogo esta vacio")
        return catalogo
    
    titulo_buscado = input("Titulo del libro:")
    libro = buscar_libro(catalogo, titulo_buscado)

    if not libro:
        print("Error: titulo no encontrado")
        return catalogo
    
    #Si encuentro el libro pedimos la operacion

    print(f"Libro encontrado: '{libro['TITULO']}' (Stock actual: {libro['CANTIDAD']})")

    while True:
        op = input("Seleccione operacion [P]restamo / [D]evolucion: ").strip().lower()

        if op == 'p':
            if libro ["CANTIDAD"] >0:
                libro ["CANTIDAD"] -=1
                print(f"Prestamos registrado. Stock restante: {libro['CANTIDAD']}")
            else:
                print("Error: no hay ejemplares disponibles para prestar")
            break #Salgo del bucle
        
        elif op == 'd':
            libro ['CANTIDAD'] += 1
            print(f"Devolucion regitrada. Stock restante: {libro['CANTIDAD']}")
            break #salgo del bucle
        
        else:
            print("Opcion no valida. intente de nuevo")

    return catalogo 

def mostrar_menu():
    #Imprime el menu de opciones
    print("\n" + "=" *30)
    print(" Gestor de biblioteca escolar")
    print("=" *30) 
    print("1. Ingresar titulos (multiples)")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catalogo")
    print("4. Consultar disponibilidad")
    print("5. Listar titulos agotados")
    print("6. Agregar titulo (individual)")
    print("7. Actualizar ejemplares (Prestamo/Devolucion)")
    print("8. Salir")
    print("-" *30)

#--- Funcion principal (MAIN) ---

def main():

    #Funcion principal que ejecuta el bucle del menu y gestiona el estado del catalogo

    catalogo = cargar_catalogo(NOMBRE_ARCHIVO)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion").strip()

        #Uso match/case segun el requisito

        match opcion:
            case "1":
                catalogo = ingresar_multiples_titulos(catalogo)
                guardar_catalogo(NOMBRE_ARCHIVO, catalogo)

            case "2":
                catalogo = ingresar_ejemplares(catalogo)
                guardar_catalogo(NOMBRE_ARCHIVO, catalogo)
            
            case "3":
                mostrar_catalogo(catalogo)

            case "4":
                consultar_disponibilidad(catalogo)

            case "5":
                listar_agotados(catalogo)

            case "6":
                catalogo = agregar_titulo_individual(catalogo)
                guardar_catalogo(NOMBRE_ARCHIVO,  catalogo)

            case "7":
                catalogo = actualizar_prestamo_devolucion(catalogo)
                guardar_catalogo(NOMBRE_ARCHIVO, catalogo)

            case "8":
                print("\nGRACIAS POR USAR EL GESTOR DE LA BIBLIOTECA")
                break #Termino el while

            case _:

                print("\nError: opcion no valida, elija un numero del 1 al 8")
            
        if opcion != "8":
            input("\n...PRESIONE ENTER PARA CONTINUAR...")

#Punto de entrada del programa
if __name__ == "__main__":
    main()