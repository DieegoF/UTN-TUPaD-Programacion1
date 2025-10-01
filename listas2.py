# 1

notas = [5, 6, 7, 3, 10, 1, 4, 6, 8, 4]

print("notas de estudiantes:", notas)

promedio = sum(notas) / len(notas)
print("promedio de notas:", promedio)

nota_maxima = max(notas)
nota_minima = min(notas)

print("nota más alta:", nota_maxima)
print("nota más baja:", nota_minima)



# 2

productos = []

for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

print("\nLista de productos ordenada alfabéticamente:")
print(sorted(productos))

eliminar = input("\nIngrese el producto que quiere eliminar: ")

if eliminar in productos:
    productos.remove(eliminar)
    print(f"\nEl producto '{eliminar}' fue eliminado")
else:
    print(f"\nEl producto '{eliminar}' no está en la lista")

print("Lista actualizada:", productos)



# 3

import random

numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista generada:", numeros)

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\nNúmeros pares:", pares)
print("Cantidad de pares:", len(pares))

print("\nNúmeros impares:", impares)
print("Cantidad de impares:", len(impares))


# 4

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

sin_repetidos = list(set(datos))

print("Lista original:", datos)
print("Lista sin repetidos:", sin_repetidos)



# 5

estudiantes = ["diego", "ana", "luis", "rocio", "rodrigo", "laura"]

print("Lista inicial:", estudiantes)

accion = input("\n¿Querés 'agregar' un estudiante o 'eliminar' uno? ")

if accion == "agregar":
    nuevo = input("Ingrese nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"\nSe agregó {nuevo} a la lista")

elif accion == "eliminar":
    borrar = input("Ingrese estudiante para eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
        print(f"\nSe eliminó a {borrar} de la lista")
    else:
        print(f"\nEl estudiante {borrar} no está en la lista")

else:
    print("\nOpción no válida. No hay cambios.")

print("\nLista final:", estudiantes)



# 6

numeros = [10, 20, 30, 40, 50, 60, 70]
print("Lista original:", numeros)

ultimo = numeros.pop()
numeros.insert(0, ultimo)

print("Lista rotada:", numeros)



# 7

temperaturas = [
    [12, 20],
    [10, 18],
    [14, 22],
    [11, 19],
    [13, 25],
    [15, 23],
    [9, 21]
]

minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)

print("Promedio de mínimas:", promedio_min)
print("Promedio de máximas:", promedio_max)

amplitudes = [fila[1] - fila[0] for fila in temperaturas]

mayor_amplitud = max(amplitudes)
dia = amplitudes.index(mayor_amplitud) + 1

print("Mayor amplitud térmica:", mayor_amplitud, "°C en el día", dia)



# 8

notas = [
    [7, 8, 9],
    [5, 2, 1],
    [3, 4, 2],
    [7, 6, 5],
    [9, 7, 6]
]

print("Promedio de cada estudiante:")
for i, fila in enumerate(notas, start=1):
    promedio_est = sum(fila) / len(fila)
    print(f"Estudiante {i}: {promedio_est:.2f}")

materias = len(notas[0])
print("\nPromedio de cada materia:")
for j in range(materias):
    columna = [fila[j] for fila in notas]
    promedio_mat = sum(columna) / len(columna)
    print(f"Materia {j+1}: {promedio_mat:.2f}")

# 9

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print("".join(fila))
    print()

print("Tablero inicial:")
mostrar_tablero()

for turno in range(2):
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"

    print(f"Turno del jugador {jugador}")
    fila = int(input("Ingrese fila (0-2): "))
    col = int(input("Ingrese columna (0-2): "))

    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador
    else:
        print("Esa casilla ya está ocupada. Pierde el turno")

    mostrar_tablero()


# 10

ventas = [
    [5, 7, 8, 2, 4, 5, 6],
    [3, 5, 6, 4, 2, 4, 6],
    [3, 6, 6, 2, 5, 7, 8],
    [10, 2, 4, 21, 2, 5, 6]
]

print("Total vendido por producto:")
totales_producto = []
for i, fila in enumerate(ventas, start=1):
    total = sum(fila)
    totales_producto.append(total)
    print(f"Producto {i}: {total}")

totales_dias = [sum(col) for col in zip(*ventas)]
mayor_ventas = max(totales_dias)
dia_max = totales_dias.index(mayor_ventas) + 1
print(f"\nDía con mayores ventas: día {dia_max} (total = {mayor_ventas})")

mas_vendido = max(totales_producto)
prod_max = totales_producto.index(mas_vendido) + 1
print(f"\nProducto más vendido: producto {prod_max} (total = {mas_vendido})")
