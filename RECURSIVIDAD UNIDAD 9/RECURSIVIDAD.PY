#ejercicio 1

def factorial(n):
    #calcular el factorial de un numero n de forma recursiva
    if n == 0 or n == 1:
        return 1
    #paso recursivo
    else:
        return n * factorial(n - 1)
    
#ejercicio 2

def fibonacci(n):
    #calcula el valor de la serie de fibonacci en la posicion 'n'(base 1)

    if n <= 1:
        return n 
    #paso recursivo
    else:
        return fibonacci(n -1) + fibonacci(n - 2)
    
#ejercicio 3
    
    def potencia(base, exponente):
        #calcula la potencia de 'base' elevada a 'exponente' de forma recursiva

        if exponente == 0:
            return 1
        #paso recursivo
        else:
            return base * potencia(base, exponente - 1)
        
#ejercicio 4

def decimal_a_binario(n):
    #convierte un numero decimal 'n' a su representacion binaria en cadena
    if n < 2:
        return str(n)
    #paso recursivo, divide por 2 y concatena el resto
    else:
        return decimal_a_binario(n //2) + str(n % 2)

#ejercicio 5

def es_palindromo(palabra):
    #verifica si una palabra es un palindromo de forma recursiva

    if len(palabra) <= 1:
        return True
    
    #paso recursivo, compara la primera y ultima letra
    if palabra[0] == palabra[-1]:
        #si es igual verifica el resto de la palabra
        return es_palindromo(palabra[1:-1])
    else:
        #si son diferentes, no es un palindromo
        return False
    
#ejercicio 6

def suma_digitos(n):
    #suma los digitos de un numero entero 'n' de forma recursiva
    if n < 10:
        return n
    #paso recursivo, suma el ultimo digito con la suma del resto del numero
    else:
        return (n%10) + suma_digitos(n //10)
    
#ejercicio 7

def contar_bloques(n):
    #calcula el numero total de bloques en una piramide

    if n == 1 :
        return 1 
    #paso recursivo
    else:
        return n + contar_bloques(n - 1)
    
#ejercicio 8

def contar_digito(numero, digito):
    #contar cuantas veces aparece un digito en un numero
    if numero == 0:
        return 0
    #comparamos el ultimo digito

    ultimo_digito = numero % 10
    conteo = 0
    if ultimo_digito == digito:
        conteo = 1

    #paso recursivo, sumo el conteo actual (0 a 1)

    return conteo + contar_digito(numero //10, digito)