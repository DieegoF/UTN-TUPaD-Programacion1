#conversion decimal a binario


#pedimos al usuario que ingrese un numero
num = input ("ingrese un numero decimal:")

#revisamos si todos los caracteres son digitos, si es valido
#convertimos a entero con int, sino mostramos error
if num.isdigit():
    n = int(num)
    if n == 0:
        print("binario: 0") #caso especial si el usuario pone 0

    #conversion manual: tomamos el resto de dividir por 2, construimos de derecha a izq.
    # hacemos la division entera //2 para seguir despues
    # el while se repite hasta que n llegue a 0    
    else:
        binario = ""
        while n > 0:
            resto = n % 2
            binario = str(resto) + binario
            n = n // 2
        print ("Binario:", binario)
else:
    print ("ERROR: ingrese un numero entero positivo") #si el usuario ingresa algo no numerico sale error

#Binario a decimal

#pedimos un numero binario como texto
b= input("ingrese un numero binario (solo 0 y 1):")

#validamos

#recorremos cada caracter, si hay distintos de 0 y 1 es invalido, sino es valido
es_valido=True
for c in b:
    if c != "0" and c != "1":
        es_valido = False
if es_valido and b != "":
    total = 0
    potencia = 0
    for digito in b [::-1]: #recorro al reves 
        total = total + int(digito)*(2**potencia) #cada digito se multiplica por una potencia de 2
        potencia = potencia + 1 #empieza en 0 e incrementa de a 1 
    print ("decimal:", total)
else:
    print("ERROR: solo 0 y 1")

#el programa convierte de decimal a binario usando divisiones
#sucesivas entre 2 y acumulando los restos
#convierte de binario a decimal multiplicando cada digito por su potencia de 2 

#tiene validaciones, en decimal solo acepta numeros enteros positivos y en binario
#solo acepta 0 y 1