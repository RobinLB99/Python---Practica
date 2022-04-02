print("Programa de evaluacion de notas des alumnos")

# La funcion input() permitira ingresar un texto por teclado. Esta tambien permite texto como parametro
nota_alumno = input("Introduce la nota del alumno: \n")

def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5 :
        valoracion = "Reprobado"
    return valoracion

# La funcion int() convertira el valor ingresado por teclado en un valor numerico, siempre y cuando sea un numero el que se ingreso, ya que input lo ingresa todo como un Strings
print(evaluacion(int(nota_alumno)))

# ----------------------------------------------------------

print('Verificacion de acceso')
