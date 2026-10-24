"""Micro-reto 3: actualizar una lista por índice con while.

Contexto: puntajes ficticios de una actividad universitaria expresados como
porcentajes. Para un análisis, se transformarán a valores entre 0 y 1.

Prediga la lista final. Complete la actualización y siga el valor del índice.
"""

puntajes = [72, 85, 90,100]
indice = 0

#Mientras o es menor a 4 
while indice < len(puntajes):
    # TODO: actualice el puntaje de esta posición dividiéndolo entre 100.
    puntajes[indice]=puntajes[indice]/100
    print(puntajes)
    print('Selección por índice: ', puntajes[indice])
    
    
    indice += 1

print("Puntajes normalizados:", puntajes)

# Resultado esperado: [0.72, 0.85, 0.9]
