miLista = ["Maria", "Juan", "Pedro", "Robin", "Jhon"]
print(miLista[2]) # Pedro
print(miLista[0]) # Maria
print(miLista[-1]) # Jhon
print(miLista[-4]) # Juan

# miLista[incluye:excluye]
print(miLista[0:3]) # Maria, Juan, Pedro
print(miLista[1:2]) # Juan

# accede a los ultimos elementos desde el indice dado hasta el final
    # miLista[desde:]
print(miLista[2:]) # Pedro, Robin, Jhon
print(miLista[3:]) # Robin, Jhon

# Para agregar elementos al final de la lista
miLista.append("Sandra")
print(miLista) # ['Maria', 'Juan', 'Pedro', 'Robin', 'Jhon', 'Sandra']

#Para agragar un elemento a la lista en el indice dado
    # miLista.insert(posicion, "Elemento")
miLista.insert(2, "Joel")
print(miLista) # ['Maria', 'Juan', 'Joel', 'Pedro', 'Robin', 'Jhon', 'Sandra']

# Para agragar varios elementos a la lista
    # miLista.extend(["Elemento1", "Elemento2", "Elemento3"])
miLista.extend(["Jefferson", "Patricia", "Genesis"])
print(miLista) # ['Maria', 'Juan', 'Joel', 'Pedro', 'Robin', 'Jhon', 'Sandra', 'Jefferson', 'Patricia', 'Genesis']

# Saber el indixe en el que se encuentra un elemento
    # miLista.index("ElementoABuscar")
print(miLista.index("Robin")) # 4
print(miLista.index("Jhon")) # 5
print(miLista.index("Genesis")) # 9

# Comprobar si un elemento se encuentra o no se encuentra en una lista
print("Antonio" in miLista) # False
print("Sandra" in miLista) # True

# Para eleminar elemento de una lista
miLista.remove("Pedro")
print(miLista) # ['Maria', 'Juan', 'Joel', 'Robin', 'Jhon', 'Sandra', 'Jefferson', 'Patricia', 'Genesis']

# Eliminar el ultimo elemento de la lista
miLista.pop()
print(miLista) # ['Maria', 'Juan', 'Joel', 'Robin', 'Jhon', 'Sandra', 'Jefferson', 'Patricia']

# Sumar listas
miLista2 = [True, "blue", 32]
miLista3 = miLista + miLista2
print(miLista3) # ['Maria', 'Juan', 'Joel', 'Robin', 'Jhon', 'Sandra', 'Jefferson', 'Patricia', True, 'blue', 32]

# Repetir lista
milista = miLista * 3
print(milista) # ['Maria', 'Juan', 'Joel', 'Robin', 'Jhon', 'Sandra', 'Jefferson', 'Patricia', 'Maria', 'Juan', 'Joel', 'Robin', 'Jhon', 'Sandra', 'Jefferson', 'Patricia', 'Maria', 'Juan', 'Joel', 'Robin', 'Jhon', 'Sandra', 'Jefferson', 'Patricia']