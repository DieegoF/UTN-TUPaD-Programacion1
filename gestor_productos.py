#Definimos funciones

def leer_y_mostrar_productos(nombre_archivo):
    print(" -- mostrando productos --")
    try: 
        #with open()manejamos el cierre automatico del archivo
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip() #sacamos espacios
                if linea: #aseguramos que no este vacia
                   nombre, precio_str, cantidad_str = linea.split(',') #separamos por ,

                   #mostramos con el formato solicitado
                   print(f"producto: {nombre} | precio: ${float(precio_str)} | cantidad: {int(cantidad_str)}")
    except FileNotFoundError:
        print(f"error: el archivo {nombre_archivo} no se encontro.")
        return False #indica que hubo un error
    print("-----------")
    return True #indica que la lectura fue exitosa

def agregar_producto_desde_teclado(nombre_archivo):
    #agregamos un nuevo producto
    print("\n-- agregar nuevo producto --")
    try:
        #pedimos datos al usuario
        nombre = input("ingrese nombre del producto:").strip()
        precio = float(input("ingrese precio:"))
        cantidad = int(input("ingrese cantidad:"))

        #validamos que no ingresen datos vacios
        if not nombre:
            print("error: el nombre no puede estar vacio")
            return
        
        #agregamos un salto de linea
        linea_nueva = f"\n{nombre}, {precio}, {cantidad}"

        #usamos 'a' (append) para agregar al final SIN borrar
        with open(nombre_archivo, 'a', encoding= 'utf-8') as f:
            f.write(linea_nueva)
        
        print(f"¡Producto '{nombre}' agregado exitosamente!")

    except ValueError:
        print("Error: precio y cantidad deben ser numeros validos.")
    except Exception as e:
        print(f"error al guardar el producto: {e}")

def cargar_productos_en_lista(nombre_archivo):

    #cargamos productos del archivo en una lista de  diccionarios,usamos ´r´ (read)

    print("\n --- cargando productos en lista de diccionarios ---")
    productos = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    nombre, precio_str, cantidad_str = linea.split(',')

                    #convertimos los datos
                    producto = {
                        "nombre": nombre,
                        "precio": float(precio_str),
                        "cantidad": int(cantidad_str)
                    }                       

                    #agregar el diccionario a la lista
                    productos.append(producto)
    except FileNotFoundError:
        print(f"error: archivo {nombre_archivo} no encontrado al cargar la lista")
    except Exception as e:
        print(f"error al procesar el archivo para la lista: {e}")

    print(f"se cargaron {len(productos)} productos en la lista de memoria")
    return productos

def buscar_producto_en_lista(lista_productos):
    #buscamos un producto por nombre

    print("\n--- buscar producto ---")
    nombre_buscar = input ("ingrese el nombre del producto a buscar: ").strip()

    encontrado = None
    for producto in lista_productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            encontrado = producto
            break #encuentro y dejo de buscar

    if encontrado:
        print("¡Producto encontrado!")
        print(f" nombre: {encontrado['nombre']}")
        print(f" precio: ${encontrado['precio']}")
        print(f" cantidad: {encontrado['cantidad']}")
    else:
        print (f"Error: producto '{nombre_buscar}' no encontrado en la lista")

def guardar_productos_actualizados(nombre_archivo, lista_productos):
    #sobreescribimos el archivo con la lista de producto usan 'w'

    print("\n--- guardando lista actualizada en archivo ---")
    try:
        with open(nombre_archivo, 'w', encoding= 'utf-8') as f:

            for i, producto in enumerate(lista_productos):
                linea = f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}"

                if i < len(lista_productos) - 1:
                    linea += "\n"

                    f.write(linea)
        print(f"archivo {nombre_archivo} actualizado con {len(lista_productos)} productos")

    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

#funcion que ejecuta el programa

def main():

    archivo_productos = "producto.txt"
    
    if not leer_y_mostrar_productos(archivo_productos): #si el archivo no eiste, no continuamos

        print("finalizando el programa por error del archivo")
        return
    
    agregar_producto_desde_teclado(archivo_productos) #pedimos al usuario un nuevo prod. y lo añadimos

    lista_de_productos = cargar_productos_en_lista(archivo_productos) # cargamos todo el archivo

    buscar_producto_en_lista(lista_de_productos) #buscamos un prooducto en la lista

    guardar_productos_actualizados(archivo_productos, lista_de_productos)  # guardamos la lista completa

    print("\n--- programa finalizado ---")

if __name__ == "__main__":
    main()

    #1- leer_y_mostrar_productos() abre el archivo en modo 'r'(lectura), recorre cada linea, la limpia
    # con .strip() y la divide con .split(',') para despues imprimirla con el formato pedido

    #2 - agregar_producto_desde_teclado() pide los datos al usuario, abre el archivo en modo 'a'(append)
    # escribe al final del archivo sin borrar lo que ya existe

    #3 - cargar_productos_en_lista() vuelve a abrir el archivo en modo 'r'para procesar cada linea,
    # crea un diccionario y lo añade a productos. 

    #4 - buscar_producto_en_lista() trabaja exclusivamente con la lista_productos que se creo en el 
    # paso anterior. Ya no lee el archivo, recorre la lista y compara nombres.

    #5 - guardar_productos_actualizados() abre el archivo en modo 'w' borra todo el contenido anterior
    # y escribe el archivo desde cero. El programa recorre lista_productos en memoria y escribe cada diccionario
    # como una linea de texto en el archivo, logrando la persistencia de datos.