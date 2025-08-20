#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.""""

print ("!Hola mundo¡")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla.

name = input("ingrese su nombre")

print (f"!Hola", name)

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla.

name= input("ingrese su nombre")
apellido= input ("ingrese su apellido")
edad= input ("ingrese su edad")
residencia= input ("ingrese su residencia")

print (f"soy", name,apellido, "tengo", edad, "soy de", residencia)

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro.

pi= 3.14

radio = int(input("Ingrese el radio: "))

area= pi * (radio * radio)
perimetro= 2* pi * radio


print (f"el area es", area)
print (f"el perimetro es", perimetro)

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale.

segundos = int(input("ingrese segundos"))

horas= segundos / 3600

print(f"{segundos} segundos equivalen a {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número. 

numero = int(input("ingrese un numero"))

print (f"tabla de multiplicar del {numero}")

for i in range (1,10):
    resultado=numero*i
    print (f"{numero} x {i} = {resultado}")

    #7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingrese un número distinto de 0 "))
numero2 = int(input("Ingrese un número distinto de 0 "))

print(f"{numero1} + {numero2} = {numero1 + numero2}")
print(f"{numero1} - {numero2} = {numero1 - numero2}")
print(f"{numero1} * {numero2} = {numero1 * numero2}")
print(f"{numero1} / {numero2} = {numero1 / numero2}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
#modo:  
#𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
#(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

altura= int(input("ingrese su altura en metros"))
peso= int(input("ingrese su peso en kg"))

mc= peso / (altura*altura)

print (f"su IMC es", mc)

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 

#T𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32


celsius = int(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (9 * celsius) // 5 + 32

print(f"La temperatura en Fahrenheit es:", fahrenheit)

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números. 

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) // 3

print("El promedio de los números es:", promedio)









