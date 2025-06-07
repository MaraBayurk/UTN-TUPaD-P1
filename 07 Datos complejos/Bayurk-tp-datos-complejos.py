# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300


precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f'El precio de las frutas es: {precios_frutas}')


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800


precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(f'El precio de las frutas es: {precios_frutas}')


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

print(precios_frutas.keys())


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo: contactos= {"juan":"123", "ana": "987"}



directorioTelefonico = {}

def guardarContacto(nombre, numero):
    directorioTelefonico[nombre] = numero
    print("Se guardo el contacto")
 
def consultarContacto(nombre):
    buscar = directorioTelefonico.get(nombre, 0)
    if(buscar):
        print(f'El numero de telefono de {nombre} es: {buscar} :)')
    else:
        print(f'No se encontró el contacto {nombre} :(')


def directorio():
    intentosMaximos = 5  
    while intentosMaximos != 0:
        opcion = int(input('Selecciona el numero de lo que queres hacer: 1) Guardar contacto, 2) Consultar contacto o 3) Salir del directorio '))

        if opcion == 1:
            nombre = input("Ingresa el nombre del contacto que queres guardar: ")
            numero = input("Ingresa el numero que queres guardar: ")
            guardarContacto(nombre, numero)
            intentosMaximos -= 1
            
        if opcion == 2:
            nombre = input("Ingresa el nombre del contacto que queres buscar: ")
            consultarContacto(nombre)
        
        if opcion == 3:
            intentosMaximos= 0
    
    return

directorio()



# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.


def frasesUnicas():
    frase = input('Dame una frase:').split()
    palabrasUnicas = set(frase)
    cantidadDeRepeticion = {}
    for palabra in frase:
        if palabra in cantidadDeRepeticion:
            cantidadDeRepeticion[palabra] += 1
        else:
            cantidadDeRepeticion[palabra] = 1
        
    
    print(f'Las palabras unicas son: {palabrasUnicas}')
    print(f'Cantidad de veces que se repiten: {cantidadDeRepeticion}')
    
frasesUnicas()


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.


alumnos = {}
promedio = {}

def ingresoAlumnos(nombre, nota1, nota2, nota3):
    alumnos[nombre]= (nota1, nota2, nota3)
    promedio[nombre]= (nota1 + nota2 + nota3)/3
    
def nombresAlumnos():
    bandera = 0
    while bandera < 3:
        nombre = input('Ingresa el nombre: ')
        nota1 = int(input('Nota 1: '))
        nota2 = int(input('Nota 2: '))
        nota3 = int(input('Nota 3: '))
        ingresoAlumnos(nombre, nota1, nota2, nota3)
        bandera += 1
    
    print(f'Los alumnos con sus notas son: {alumnos}')
    print(f'Los promedios son {promedio}')
        
nombresAlumnos()
    

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


primerParcial = {5,9,6,10,8}
segundoParcial={8,6,10,5,7}

def mostrarDatos():
    aprobadosAmbosParciales = primerParcial.intersection(segundoParcial)
    print(f'Los alumnos que aprobaron ambos parciales son: {aprobadosAmbosParciales}')
    
    aprobadosUnParcial = primerParcial.symmetric_difference(segundoParcial)
    print(f'Los alumnos que aprobaron solo un parcial son: {aprobadosUnParcial}')
    
    aprobadosAlMenosUnParcial = primerParcial.union(segundoParcial)
    print(f'Los alumnos que aprobaron al menos un parcial son: {aprobadosAlMenosUnParcial}')

mostrarDatos()


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {
    "arroz": 4,
    "fideos": 10,
    "pure": 3 
}

def consultarStock(producto):
    if producto in productos:
        print(f'El stock de {producto} es {productos[producto]}')
    else:
        print(f'El producto {producto} no existe en el inventario')

def agregarProductoStock(producto, stock):
    if producto in productos:
        productos[producto] += stock
        print(f'Agregamos stock del {producto}, sumamos el {stock}, ahora tenes {productos[producto]}')
    else:
        producto[producto] = stock
        print(f'Agregamos el producto {producto} con el stock {stock}')
    
    print(f'Los productos son {productos}')

consultarStock('pure')
agregarProductoStock('pure', 10)


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#     Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de ingles",
    ("jueves", "09:00"): "Clase de matematica",

}

def consultarAgenda(dia, hora):
    fecha = (dia, hora)
    for horario in agenda:
        if horario == fecha:
            print(f'La actividad es: {agenda[fecha]}')
            return
    print(f'Esa actividad no existe')
    return
            
consultarAgenda('jueves', '09:00')


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}

def invertirClaveValor():
    nuevoDiccionario = dict()
    for pais, capital in original.items():
        nuevoDiccionario[capital] = pais
    print(nuevoDiccionario)
    
invertirClaveValor()