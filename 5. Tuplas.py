# Las tuplas son listas inmutalbes. es decir, listas que no se pueden modificar despues de su creacion.
# Si permiten extraer porsiones, pero el resultado sera otra Tupla.
# Si permite comprobar si un elemento existe en la Tupla.
# Las Tuplas son mas rapidas, utilizan menos espacios, formatean Strings y pueden utilizarse como claves en un diccionario.

# miTupla = (Elemento1, Elemento2, Elemento3.....)

miTupla = ("Robin", 2,11,1999, "Robin")
print(miTupla) # ('Robin', 2, 11, 1999, 'Robin')
print(miTupla[2]) # 11

# Convertir una Tupla en lista
miLista = list(miTupla)
print(miLista) # ['Robin', 2, 11, 1999, 'Robin']

# Convertir una lista en Tupla
miTupla2 = tuple(miLista)
print(miTupla2) # ('Robin', 2, 11, 1999, 'Robin')

# Determina si existe un elemento en la Tupla en lista
print("Robin" in miTupla) # True
print("Joel" in miTupla) # False

# Cuenta cuantas veces se encuantra un elemento dentro de la Tupla
print(miTupla.count("Robin")) # 2

# Nos permite saber la longitud de una Tupla
print(len(miTupla)) # 5

# Tupla Unitaria --- miTupla("Elemento",)
miTupla2 = ("Joel",)
print(miTupla2) # ('Joel',)
print(len(miTupla2)) # 1

# Empaquetado de Tupla. (Se puede declarar una Tupla sin parentesis)
miTupla3 = "Joel", 12, 2, 2000
print(miTupla3) #('Joel', 12, 2, 2000)

# Desempaquetado de Tupla
nombre, day, month, year = miTupla3
print(nombre) # 'Joel'
print(day) # 12
print(month) # 2
print(year) # 2000

