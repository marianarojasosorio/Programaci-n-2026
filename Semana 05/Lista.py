"""Microreto: el portero del café."""
#Mariana Rojas

#Entrada

nombre=input('Como te llamas?:').upper().strip()
energia=int(input('Cuánta energía tienes de 0 100:?'))
traecafe=input('Traes café (si/no): ').lower().strip()=='si'

#Si tengo menos del 50% y no tengo café - Descanso
#Si tengo 50% de energía o más o tengo café-Puede ingresar a la clase
#Otro Escenario : Portero confundido: revisar respuestas
mensaje='Condiciones para ingresar'

if energia<50 and not(traecafe):
    mensaje='Acceso denegado, ve a descansar'
elif energia>=50 or traecafe:
    mensaje='Puede ingresar a la clase'
else:
    mensaje='Portero confundido, revisar respuestas'

print(f'{nombre}:{mensaje}')