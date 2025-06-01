# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo ():
    print("¡Hola, mundo!")

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"¡Hola, {nombre}!")
    
# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
    
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

    
    
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.


def calcular_area_circulo(radio):
    import math
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    import math
    perimetro = 2 * math.pi * radio
    return perimetro



# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division =  a/b
    return (suma, resta, multiplicacion, division)
    

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio



def ejecutarFunciones():

    # 1
    print("----Ejecicio 1 Imprimir Hola Mundo----")
    imprimir_hola_mundo()
    print("--------------------------------------")
    
    
    # 2
    print("----Ejecicio 2 Saludar Usuario----")
    nombre_usuario = input("Ingrese su nombre: ")
    saludar_usuario(nombre_usuario)
    print("--------------------------------------")
    
    
    # 3
    print("----Ejecicio 3 Información Personal----")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    informacion_personal(nombre_usuario, apellido, edad, residencia)
    print("--------------------------------------")
   
   
    # 4
    print("--------------------------------------")
    print("----Ejecicio 4 Calcular Área y Perímetro de un Círculo----")
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El área del círculo es: {area}")
    print(f"El perímetro del círculo es: {perimetro}")
    print("--------------------------------------")
   
    
    # 5
    print("----Ejecicio 5 Convertir Segundos a Horas----")
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"La cantidad de horas es: {horas}")
    print("--------------------------------------")
    
    
    #6
    print("----Ejecicio 6 Tabla de Multiplicar----")
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)
    print("--------------------------------------")
    
    
    #7
    print("----Ejecicio 7 Operaciones Básicas----")
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    resultados = operaciones_basicas(numero1, numero2)
    print(f"Resultados:\nSuma: {resultados[0]}\nResta: {resultados[1]}\nMultiplicación: {resultados[2]}\nDivisión: {resultados[3]}")
    print("--------------------------------------")
    
    
    #8
    print("----Ejecicio 8 Calcular IMC----")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su índice de masa corporal (IMC) es: {imc}")
    print("--------------------------------------")
    
    
    #9
    print("----Ejecicio 9 Convertir Celsius a Fahrenheit----")
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"La temperatura en Fahrenheit es: {fahrenheit}")
    print("--------------------------------------")
    
    
    #10
    print("----Ejecicio 10 Calcular Promedio----")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(a, b, c)
    print(f"El promedio de los números es: {promedio}")
    
ejecutarFunciones()
    
    