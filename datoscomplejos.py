#1 agregar frutas al diccionario

precios_frutas = {'banana': 1200, 'anana': 2500, 'melon': 3000, 'uva': 1450}

precios_frutas['naranja'] = 1200
precios_frutas['manzana'] = 1500
precios_frutas['pera'] = 2300

print(precios_frutas)

#2 Precios

precios_frutas['banana'] = 1330
precios_frutas['manzana'] = 1800
precios_frutas['melon'] = 1290

print(precios_frutas)

#3 Crear lista solo frutas

frutas = list(precios_frutas.keys())

print(frutas)

#4 agenda de contactos

contactos = {}

for i in range(5):
    nombre=input("nombre: ")
    numero=input("numero: ")
    contactos[nombre] = numero

nombre_buscar = input("ingre el nombre a consultar: ")

if nombre_buscar in contactos:
    print(f"el numero de {nombre_buscar} es {contactos[nombre_buscar]}")
else:
    print("contacto no encontrado")

#5 frases

frase = input ("escribi una frase: ").lower() .split()

palabras_unicas = set(frase)

recuento = {}
for palabra in frase:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("palabras unicas: ", palabras_unicas)
print("recuento:", recuento)

#6 promedio

alumnos = {}

for i in range(3):
    nombre = input("nombre del alumno:")
    notas = tuple(float(input(f"nota {j+1}:")) for j in range (3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) /len(notas)
    print(f"{nombre}) - promedio: {promedio:,2f}")

#7 aprobados

parcial1= {1,2,3,4,5}
parcial2= {4,5,6,7,8}

ambos = parcial1 & parcial2

solo_uno= parcial1 ^ parcial2

al_menos_uno = parcial1 | parcial2

print("aprobaron ambos:", ambos)
print("aprobaron solo uno:", solo_uno)
print("aprobaron al menos uno:", al_menos_uno)

#8 stock

stock = {}

while True:
    producto = input("producto:")


    if producto in stock:
        agregar = int(input("cuanto agregar al stock:"))
        stock[producto] += agregar
    else:
        nuevo = int(input("no existe, indique cantidad:"))
        stock[producto] = nuevo

    continuar = input("¿Desea continuar? (s/n)").lower()
    if continuar != 's':
        break
    
consulta = input ("consultar stock de:")
if consulta in stock:
    print(f"stock de {consulta}: {stock[consulta]}")
else:
    print("producto no encontrado.")

#9 agenda con tuplas

agenda = {
    ('lunes', '10:00'): 'reunion',
    ('martes', '15:00'): 'ingles'
}

dia = input("dia:")
hora = input("hora:")

if (dia,hora) in agenda:
    print(f"actividad: {agenda[dia,hora]}")
else:
    print("no hay actividades")

#10 invertir diccionario

original = {"Argentina": "buenos aires", "Chile": "Santiago", "Peru": "Lima"}

invertido = {capital: pais for pais, capital in original.items()}

print(invertido)
