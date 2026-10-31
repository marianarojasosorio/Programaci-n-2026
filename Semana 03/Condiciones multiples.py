#Leer una nota, si la nota es igual o mayo a 90 es excelente
#Si la nota es mayor a 80 es muy bueno
# Nota mayor o igual a 70 es aprobadoy cualquier nota inferior a 70
# Es un reprobado

nota=float(input('Incluir una nota de 0-100: '))

if(nota>100) or (nota<0):
    print('Error número no válido')
else:
    if nota >= 90:
        print('Excelente')
    elif nota > 80:
        print('Muy bien')
    elif nota >= 70:
        print('Aprobado')  
    else:
        print('Reprobado')
    

