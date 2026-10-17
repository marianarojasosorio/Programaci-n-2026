#Ejercicio cafe semana 05

producto=['Cafe',5000,20]

porcentajeaumento=20

#proceso de datos

descuento=producto[1]*15/100
preciopromocional=producto[1]*-descuento
ingresoactual=producto[1]*producto[2]
unidadesproyectadas=(producto[2]*porcentajeaumento/100)+producto[2]
ingresosproyectados=(preciopromocional*unidadesproyectadas)-ingresoactual

if ingresosproyectados>0:
    recomendacion='Lanzar'
else:
    recomendacion='No lanzar'



    
