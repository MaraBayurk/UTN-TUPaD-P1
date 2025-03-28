# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")



# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input('¿Cómo te llamas? ')
print(f'Hola {nombre}!')





#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input('¿Cómo te llamas? ')
apellido = input('¿Cuál es tu apellido? ')
edad = input('¿Cuántos años tienes? ')
residencia = input('¿Dónde vives? ')
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")





# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = input('Introduce el radio de un círculo: ')
pi = 3.1416
area = pi * float(radio) ** 2
perimetro = 2 * pi * float(radio)
print(f"El área de un círculo de radio {radio} es {area}")
print(f"El perímetro de un círculo de radio {radio} es {perimetro}")





# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = input('Introduce una cantidad de segundos: ')
horas = int(segundos) / 3600
print(f"{segundos} segundos equivalen a {horas} horas")





# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número

numero = int(input('Introduce un número: '))
for i in range(11):
    print(f"{numero} x {i} = {numero * i}")
  
  
  
    

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.  

numero1 = int(input('Introduce un número distito de 0: '))
if numero1 == 0:
    numero1 = int(input('El nùmero ingresado es incorrecto, por favor introduce un número distito de 0: '))

numero2 = int(input('Introduce otro número distinto de 0: '))
if numero2 == 0:
    numero2 = int(input('El nùmero ingresado es incorrecto, por favor introduce un número distito de 0: '))

if numero1 == 0 or numero2 == 0:
    print("Los números ingresados son incorrectos. Por favor introduce números distintos de 0")
    
else:
    print(f"La suma de {numero1} y {numero2} es {numero1 + numero2}")
    print(f"La resta de {numero1} y {numero2} es {numero1 - numero2}")
    print(f"El producto de {numero1} y {numero2} es {numero1 * numero2}")
    print(f"La división de {numero1} y {numero2} es {numero1 / numero2}")





# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.

altura = float(input('Introduce tu altura en metros: '))
peso = float(input('Introduce tu peso en kilogramos: '))
imc = peso / altura ** 2
print(f"Tu índice de masa corporal es {imc}")





# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =
# 9/5. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celsius = float(input('Introduce una temperatura en grados Celsius: '))
fahrenheit = 9/5 * celsius + 32
print(f"{celsius} °C son {fahrenheit} °F")





# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

numero1 = float(input('Introduce el primer número: '))
numero2 = float(input('Introduce el segundo número: '))
numero3 = float(input('Introduce el tercer número: '))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de {numero1}, {numero2} y {numero3} es {promedio}")



