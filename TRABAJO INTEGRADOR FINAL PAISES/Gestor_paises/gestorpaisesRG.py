
def leer_csv(nombre_archivo):
    paises = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    for i in range(1, len(lineas)):
        linea = lineas[i].strip()
        if linea == "":
            continue  # salta líneas vacías
        partes = linea.split(",")
        if len(partes) < 4:
            print(f"Línea ignorada (incompleta): {linea}")
            continue  # salta líneas con menos de 4 valores
        try:
            pais = {
                "nombre": partes[0],
                "poblacion": int(partes[1]),
                "superficie": int(partes[2]),
                "continente": partes[3]
            }
            paises.append(pais)
        except ValueError:
            print(f"Línea ignorada (valores inválidos): {linea}")
            continue
    return paises



def guardar_csv(nombre_archivo, paises):
    archivo = open(nombre_archivo, "w")
    archivo.write("nombre,poblacion,superficie,continente\n")
    for p in paises:
        linea = p["nombre"] + "," + str(p["poblacion"]) + "," + str(p["superficie"]) + "," + p["continente"] + "\n"
        archivo.write(linea)
    archivo.close()


def agregar_pais(paises):
    nombre = input("Nombre del pais: ")
    poblacion = int(input("Poblacion: "))
    superficie = int(input("Superficie (km²): "))
    continente = input("Continente: ")
    pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    paises.append(pais)
    print(nombre + " agregado correctamente.")


def actualizar_pais(paises):
    nombre = input("Pais a actualizar: ")
    encontrado = False
    for p in paises:
        if p["nombre"] == nombre:
            p["poblacion"] = int(input("Nueva poblacion: "))
            p["superficie"] = int(input("Nueva superficie: "))
            print(nombre + " actualizado correctamente.")
            encontrado = True
    if not encontrado:
        print("Pais no encontrado.")


def buscar_pais(paises):
    nombre = input("Pais a buscar: ")
    encontrado = False
    for p in paises:
        if nombre in p["nombre"]: 
            print(p)
            encontrado = True
    if not encontrado:
        print("No se encontraron coincidencias.")


def filtrar_por_continente(paises):
    continente = input("Continente: ")
    encontrados = []
    for p in paises:
        if p["continente"] == continente:
            encontrados.append(p)
    if len(encontrados) == 0:
        print("No se encontraron paises.")
    else:
        for p in encontrados:
            print(p)


def ordenar_por_nombre(paises):
    n = len(paises)
    for i in range(n):
        for j in range(0, n-i-1):
            if paises[j]["nombre"] > paises[j+1]["nombre"]:
                temp = paises[j]
                paises[j] = paises[j+1]
                paises[j+1] = temp
    for p in paises:
        print(p)


def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return
    mayor = paises[0]
    menor = paises[0]
    total_poblacion = 0
    total_superficie = 0
    continentes = {}
    for p in paises:
        if p["poblacion"] > mayor["poblacion"]:
            mayor = p
        if p["poblacion"] < menor["poblacion"]:
            menor = p
        total_poblacion += p["poblacion"]
        total_superficie += p["superficie"]
        c = p["continente"]
        if c in continentes:
            continentes[c] += 1
        else:
            continentes[c] = 1
    promedio_poblacion = total_poblacion // len(paises)
    promedio_superficie = total_superficie // len(paises)
    print("Pais con mayor poblacion:", mayor["nombre"])
    print("Pais con menor poblacion:", menor["nombre"])
    print("Promedio de poblacion:", promedio_poblacion)
    print("Promedio de superficie:", promedio_superficie)
    print("Cantidad de paises por continente:", continentes)


def menu():
    paises = leer_csv("paises.csv")
    while True:
        print("\n=== Gestion de Paises ===")
        print("1. Agregar pais")
        print("2. Actualizar pais")
        print("3. Buscar pais")
        print("4. Filtrar por continente")
        print("5. Ordenar por nombre")
        print("6. Estadisticas")
        print("7. Guardar y salir")
        opcion = input("Seleccione opcion: ")
        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_por_continente(paises)
        elif opcion == "5":
            ordenar_por_nombre(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            guardar_csv("paises.csv", paises)
            print("Datos guardados. Saliendo")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    menu()
