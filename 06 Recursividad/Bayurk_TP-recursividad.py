# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario


def factorialNum(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorialNum(n-1)
    
def mostrarFactorialHasta(numero):
    for i in range(1, numero + 1):
        print(f'El factorial de {i} es {factorialNum(i)}')

num = int(input('ingresa el numero a factorizar: '))
mostrarFactorialHasta(num)


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.
# finonacci de un numero es la suma de el anterior de numero  + el anterior del anterior F(n)= F(n-1)+F(n-2)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1 
    else: return fibonacci(n-1) + fibonacci(n-2)
   
def mostrarFibonacci(numF):
    secuencia = []
    for i in range(numF):
        secuencia.append(fibonacci(i))
    
    print(f'La secuencia es: {secuencia}')
    print(f'El resultado es: {sum(secuencia)}')
    
    
numF = int(input('Ingresa el numero: ')) 
mostrarFibonacci(numF)


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.


def potencia(num, exponente):
    if num == 1:
        return 1
    elif exponente == 0:
        return 1
    else: return num * potencia(num, exponente-1)

def showPotenciaExponente(numP, exp):
    result = potencia(numP, exp)
    print(f'La potencia de {numP} elevado a {exp} es: ', result)
    
numP = int(input('Ingresa el numero: '))
exp = int(input('Ingresa el exponente: '))

showPotenciaExponente(numP, exp)


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.


def decimalABinario(numB):
    if numB == 0:
        return ''
    else:
        return decimalABinario(numB//2) + str(numB % 2) #hacemos // que hace divisiones enteras 13/2= 6, resto 1

def showDecimalBinario(numB):
    return print(f"el numero binario es: {decimalABinario(numB)} y en decimal: {numB}")

numBinario= int(input("ingresa el numero a convertir: "))
showDecimalBinario(numBinario)

    
# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.


def es_palindromo(palabra): #MARA
    if len(palabra) == 0 or len(palabra)== 1:
        return True
    
    indice = 0
    if palabra[indice] == palabra[len(palabra)-1]:
        return es_palindromo(palabra[1:-1])
    else: 
        return False
    

palabraP= input('Ingresa la palabra: ')
print(es_palindromo(palabraP))


# 6. Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.


def suma_digitos(n):
    if n < 10:
        return n
    
    resto = n%10
    divisionEntera = n//10 
    
    return suma_digitos(divisionEntera) + resto

numSum = int(input('Ingresa el numero: '))
print(f'La suma de digitos es: {suma_digitos(numSum)}')
    
    
# 7. Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.


def contar_bloques(n):
    if n == 1:
        return 1
    return contar_bloques(n-1) + n

bloques = int(input('Ingresa cantidad de loques: '))
print(f'la cantidad total de bloques son: {contar_bloques(bloques)}')


# 8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 
# contar_digito(8, 5) → 0


def contar_digitos(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    
    ultimoDigitDelNumero = numero % 10
    restoDelNumero = numero // 10
    
    if ultimoDigitDelNumero == digito:
        return contar_digitos(restoDelNumero, digito) + 1
    else:
        return contar_digitos(restoDelNumero, digito)
    
numeroAContar = int(input('Ingresa el numero: '))
digito = int(input('Ingresa el digito: '))
print(f'la cantidad digitos son: {contar_digitos(numeroAContar, digito)}')
  
