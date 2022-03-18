# Una funcion se la define de la siguiente manera:
#   def nombre_funcion():
#       instruccion1
#       instruccion2
#       return (opcional)

from cgitb import html


def mensaje(): #declaracion
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo instrucciones basicas")
    print("Poco a poco vamos avanzando")

print("Primera llamada")
mensaje() #Llamada
print("Segunda llamada")
mensaje()
print("Tercera llamada")
mensaje()

#-------------------------------------------------------------
print("--------------------------------------------------------------")

def suma():
    num1 = 5
    num2 = 7
    return num1 + num2

print(suma())
print(suma() + 5)
print(suma() * 5 - 4)
print(suma() + 4 / 2)

def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

almacenarResultado = multiplicacion(5,4)

print(almacenarResultado)
print(multiplicacion(5,4))