import math

# 1
def imprimir_hola_mundo():
    print("hola mundo!")

# 2
def saludar_usuario(nombre: str) -> str:
    return f"hola {nombre}!"

# 3
def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str) -> None:
    print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4
def calcular_area_circulo(radio: float) -> float:
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio: float) -> float:
    return 2 * math.pi * radio

# 5
def segundos_a_horas(segundos: float) -> float:
    return segundos / 3600.0

# 6
def tabla_multiplicar(numero: int) -> None:  # corregido nombre
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7
def operaciones_basicas(a: float, b: float) -> tuple:
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = None if b == 0 else a / b
    return (suma, resta, multiplicacion, division)

# 8
def calcular_imc(peso: float, altura: float) -> float:
    if altura <= 0:
        raise ValueError("la altura debe ser mayor a 0 metros")
    return peso / (altura ** 2)

# 9
def celsius_a_fahrenheit(celsius: float) -> float:
    return celsius * 9.0 / 5.0 + 32.0

# 10
def calcular_promedio(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3.0


# ================= PRUEBAS ================= #
print("1) imprimir_hola_mundo():")
imprimir_hola_mundo()
print()

print("2) saludar_usuario('Marcos') ->", saludar_usuario("Marcos"))
print()

print("3) informacion_personal('Ana', 'Pérez', 25, 'Córdoba') ->")
informacion_personal("Ana", "Pérez", 25, "Córdoba")
print()

radio = 5
print(f"4) calcular_area_circulo({radio}) =", round(calcular_area_circulo(radio), 2))
print(f"   calcular_perimetro_circulo({radio}) =", round(calcular_perimetro_circulo(radio), 2))
print()

segundos = 7200
print(f"5) segundos_a_horas({segundos}) =", segundos_a_horas(segundos))
print()

numero = 3
print(f"6) tabla_multiplicar({numero}):")
tabla_multiplicar(numero)
print()

a, b = 10, 5
print(f"7) operaciones_basicas({a}, {b}) ->", operaciones_basicas(a, b))
print()

peso, altura = 70, 1.75
print(f"8) calcular_imc({peso}, {altura}) =", round(calcular_imc(peso, altura), 2))
print()

celsius = 20
print(f"9) celsius_a_fahrenheit({celsius}) =", round(celsius_a_fahrenheit(celsius), 2))
print()

a, b, c = 8, 7, 9
print(f"10) calcular_promedio({a}, {b}, {c}) =", calcular_promedio(a, b, c))
print()

print("=== FIN DE LAS PRUEBAS ===")
input("\nPresioná Enter para cerrar el programa...")