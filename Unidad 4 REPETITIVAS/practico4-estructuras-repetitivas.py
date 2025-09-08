#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (0,101):
    print (i)


# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

num = int(input("ingrese un numero"))
num_str= str(abs(num))

cantidad_digitos = len(num_str)

print ("el numero", num, "tiene", cantidad_digitos, "digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 

a= int(input("ingrese el primer numero"))
b=int(input("ingrese el segundo numero"))

menor= min (a,b)
mayor= max(a,b)

total=0

for i in range  (menor +1, mayor):
    total += i

print ("la suma de los numeros entre", a, "y", b, "es:", total)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.


total=0

print ("ingrese numeros entero para sumar (ingrese 0 para terminar):")

while True:
    num=int(input("numero:"))
    if num == 0:
        break
    total += num

    print ("la suma total es:", total)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

print ("jugador 1: elige un numero entre 0 y 9")
secreto= int(input("numero secreto:"))

print ("jugador 2: adivina el numero entre 0 y 9")

intentos = 0
adivinado = False

while not adivinado:
    numero = int(input("ingresa tu intento:"))
    intentos += 1

if numero== secreto:
    adivinado= True
else:
    print ("X no es correcto, intentar de nuevo")

print ( "!Correcto! el numero era {secreto}")
print (" lo lograste en {intentos}")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 

for i in range (100, -1, -2):
    print (i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario. 

n = int (input("ingrese un numero entero positivo"))

total = 0
for i in range (0, n + 1):
    total += 1

print ( "la suma de los numeros de 0 hasta", n, "es", total)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

n = 100

pares = 0 
impares = 0
positivos = 0 
negativos = 0

print ("ingrese {n} numeros enteros:")

for i in range (n):
    num = int(input(f"numero {i+1}:"))

    if num % 2 == 0:
        pares +=1
    else: 
        impares +=1

        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1

print ("\n resultados")
print (" cantidad de pares", pares)
print (" cantidad de impares", impares)
print ("cantidad de positivos", positivos)
print (" cantidad de negativos", negativos)

#9)  Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

n= 100 

suma = 0

print ("ingrese {n} numeros enteros:")

for i in range (n):
    num = int(input("numero {i+1}:"))
    suma += num 

media = suma / n

print ("\n resultados:")
print ("suma:", suma)
print ("media:", media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

num = int(input("ingrese un numero entero:"))

#uso slicing para acceder a una subcadena de manera negativa para recorrer la secuencia
# de los digitos al reves como pide el enunciado

invertido = str(num)[::-1]

print ("numero invertido:", invertido)
