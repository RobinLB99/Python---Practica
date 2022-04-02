print('Verificacion de acceso')

edad_usuario = int(input('Introduce tu edad: '))

if edad_usuario < 18:
    print('No puedes pasar')
elif edad_usuario > 100:
    print('La edad no es correcta')
else:
    print('Puedes pasar')

print('El programa ha finalizado')


# ------------------------------------------------------
print('\n\nNotas de alumnos')

notas = int(input('Introduce tu nota: '))
print(notas)

if notas < 0:
    print('La nota no puede ser menor a 0')
elif notas < 7:
    print('Insuficiente')
elif notas <= 8:
    print('Suficiente')
elif notas == 9:
    print('Notable')
elif notas == 10:
    print('Sobresaliente')
else:
    print('La nota no puede ser mayor a 10')

print('El programa ha finalizado')