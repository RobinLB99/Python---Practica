#  1. Crea un programa que pida dos números por teclado. El programa tendrá
# una función llamada “DevuelveMax” encargada de devolver el número más
# alto de los dos introducidos.

print('\nDevuelve el numero mayor\n')
num1 = int(input('Ingresa el primer numero: '))
num2 = int(input('Ingresa el segundo numero: '))

def devuelveMax(primero, segundo):
    if primero > segundo:
        return print("Respuesta: " + repr(primero) + " es mayor que " + repr(segundo) +"\n")
    else:
        return print("Respuesta: " + repr(segundo) + " es mayor que " + repr(primero) + "\n")

devuelveMax(num1, num2)

# 2. Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos
# deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
# personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).

datosPersonales = []

nombre = print(input("Ingresa tu nombre: "))
direccion = print(input("Ingresa tu direccion: "))
telefono = print(input('Ingresa tu telefono: '))

datosPersonales.insert(0, nombre)
datosPersonales.append(direccion)
datosPersonales.append(telefono)

print(datosPersonales)


# 3. Crea un programa que pida tres números por teclado. El programa imprime en consola
# la media aritmética de los números introducidos.
