# Son extructuras de datos que no permiten almacenar valores de diferentes tipos (enteros, cadenas de texto, decimales) e incluso listas y otros diccionarios.
# Los datos se almacenan asociados a una clave de tal forma que se crea una asociacion tipo clave : valor para cada elemento almacenado.
# Los elementos almacenados no estan ordenados. El oreden es indiferente a la hora de almacenar informacion en un diccionario.

miDiccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "Ecuador":"Quito"}

print(miDiccionario["Ecuador"]) # Quito
print(miDiccionario["Francia"]) # Paris

print(miDiccionario) # {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "Ecuador":"Quito"}

# Agregar una clave y valor al diccionario -------------
miDiccionario["Italia"] = "Lisboa"

print(miDiccionario) # {'Alemania': 'Berlin', 'Francia': 'Paris', 'Reino Unido': 'Londres', 'Ecuador': 'Quito', 'Italia': 'Lisboa'}

# Modificar el valor de una clave. (Se sobreescribe)-------------------
miDiccionario["Italia"] = "Roma"

print(miDiccionario) # {'Alemania': 'Berlin', 'Francia': 'Paris', 'Reino Unido': 'Londres', 'Ecuador': 'Quito', 'Italia': 'Roma'}

# Eliminar un elemento -----------------------
del miDiccionario["Reino Unido"]

print(miDiccionario) # {'Alemania': 'Berlin', 'Francia': 'Paris', 'Ecuador': 'Quito', 'Italia': 'Roma'}

# ----------------------------------------------------------------

diccionario2 = {"Ecuador": "Guayaquil", 22:"Robin", "Lugo":99}
print(diccionario2) # {'Ecuador': 'Guayaquil', 22: 'Robin', 'Lugo': 99}

# Utilizar una Tupla para accignar una clave a cada uno de los valores -----------------
miTupla = ["España", "Francia", "Ecuador", "Mexico"]
diccionario3 = {miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Quito", miTupla[3]:"Mexico"}
print(diccionario3) # {'España': 'Madrid', 'Francia': 'Paris', 'Ecuador': 'Quito', 'Mexico': 'Mexico'}
print(diccionario3["Francia"]) # Paris
print(diccionario3[miTupla[1]]) # Paris

# Diccionario que almacena una Tupla-------------------------
diccionario4 ={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991, 1992,1993,1996, 1997, 1998]}
print(diccionario4) # {23: 'Jordan', 'Nombre': 'Michael', 'Equipo': 'Chicago', 'anillos': [1991, 1992, 1993, 1996, 1997, 1998]}
print(diccionario4["Nombre"]) # Michael
print(diccionario4["anillos"]) # [1991, 1992, 1993, 1996, 1997, 1998]

# Diccionario que almacena otro diccionario --------------------------------
diccionario5 ={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"Temporadas":[1991, 1992,1993,1996, 1997, 1998]}}
print(diccionario5) # {23: 'Jordan', 'Nombre': 'Michael', 'Equipo': 'Chicago', 'anillos': {'Temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}}
print(diccionario5["anillos"]) # {'Temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}

# Metodo que devuelve las claves de un diccionario ------------------------------
print(diccionario5.keys()) # dict_keys([23, 'Nombre', 'Equipo', 'anillos'])

# Metodo que devuelve los valores del diccionario -------------------------------
print(diccionario5.values()) # dict_values(['Jordan', 'Michael', 'Chicago', {'Temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}])

# Metodo que devuelve la longitud del diccionario -----------------------------
print(len(diccionario5)) # 4

