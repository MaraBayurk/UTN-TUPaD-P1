# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)
    
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = input("Ingrese un número: ")
print(f"El número {numero} tiene {len(numero)} dígitos.")



# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

primerNumero = int(input("Ingrese el primer número: "))
segundoNumero = int(input("Ingrese el segundo número: "))
suma = 0

for i in range(primerNumero + 1, segundoNumero):
    suma += i

print(f"La suma de los números entre {primerNumero} y {segundoNumero} es: {suma}")



# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.


numeroDeCorte = 0
suma = 0

while True:
    numeroASumar = int(input("Ingrese un número a sumar (0 para salir): "))
    print(f"El número ingresado es: {numeroASumar}")
    if numeroASumar == 0:
        break
    else:
        suma += numeroASumar
        
print(f"La suma de los números es: {suma}")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


import random

intentos = 0
numRandom = random.randint(1, 10)
print(numRandom)  # Para verificar el número aleatorio generado

while True:
    intentos += 1
    numero = int(input("Ingresa un numero enre 1 y 10: "))
    if numero == numRandom:
        print(f"Ganaste en {intentos} intentos")
        break
    else:
        print("Perdiste, intenta de nuevo")
        

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for num in range(100, -1, -2):
    print(num)
    
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numeroIngresado = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(0, numeroIngresado + 1):
    suma += i
    
print(f"La suma de los números enteros desde 1 hasta {numeroIngresado} es: {suma}")


# 8) Escribe un programa que permita al usuario ingresar 10 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos.

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(10):
    numero = int(input("Ingrese un número entero: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
        
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

from statistics import median

sumaNumeros = 0
cantidadNumeros = 0
for i in range(10):
    numero = int(input("Ingrese un número entero: "))
    sumaNumeros += numero
    cantidadNumeros += 1
print(f"La media es {sumaNumeros / cantidadNumeros}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número: ")
str(numero)
numeroInvertido = str(numero)[::-1]
print(f"El número invertido es: {numeroInvertido}")


