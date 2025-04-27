#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

numeros = list(range(4,101,4))
print(f"Números del 1 al 100 que son múltiplos de 4: {numeros}")



# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 

listaDeCincoElementos = ["asado", "pizza", "hamburguesa", "milanesa", "fideos"]
print(f"El penúltimo elemento de la lista es: {listaDeCincoElementos[-2]}")



# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.

listaVacia = []
listaVacia.append("asado")
listaVacia.append("pizza")
listaVacia.append("hamburguesa")

print(f"Lista resultante: {listaVacia}")



# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"

print(f"Lista de animales: {animales}")



# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# este programa crea una lista de números de 5 elementos y luego elimina el número máximo de la lista utilizando la función max() y remove().



# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

listaDe30Numeros = list(range(10, 31, 5))
print(f"Lista de números del 10 al 30: {listaDe30Numeros}")
print(f"Los dos primeros números son: {listaDe30Numeros[:2]}")




# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fiesta"
autos[2] = "focus"
print(f"Lista de autos: {autos}")



# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(f"Lista de dobles: {dobles}")



# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(f"Lista de compras: {compras}")




# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(f"Lista anidada: {lista_anidada}")