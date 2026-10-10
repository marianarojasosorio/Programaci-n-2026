#Misión kit segurp

nombre=input('Nombre:').upper().strip()
Kit=input('Tipo de kit:').lower().strip()
autorizacion=input('Tiene autorización (si/no)').lower().strip()== 'si'
try:
    cantidad=int(input('Cantidad de kits?: '))
except valueError:
                 print('Cantidad de kits invalida, digite del 1 al 100')
                 cantidad=-1
dias=int(input('Días de préstamo:'))

try:cantidad=int(input('Cantidad de días:'))
except valueError:
    print('Cantidad de días inválido, digite del 1 al 100')
    cantidad=-1

if not nombre or not kit or cantidad<1 or dias<1:
    resultado= 'Registro rechazado, revise lo datos ingresados'

elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado= f'Solicitud aprobada, {nombre}: {3} kit(s)'
else:
    resultado= 'Solicitud enviada a revisión'

print(resultado)
