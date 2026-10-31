#Entrada de datos

montodelacuenta=int(input('ingrese monto de la cuenta:'))
antecedentes=input('Tiene antecedentes penales: ')
profesion=input('Ingrese su profesión')

#Proceso
if(montodelacuenta<-1):
    print('valor inválido')
else:
    
    if(montodelacuenta>=50000 and antecedentes=='no') or (profesion=='diplomatico'):
        print('Aprobado, visa dorada')
    elif(montodelacuenta>=20000 and antecedentes=='no'):
        print('Aprobado: visa estándar')
    elif(montodelacuenta<=20000 and profesion=='estudiante' or profesion=='jubilado'):
         print('Pendiente entrevista')
    else:
        print('Denegado')
        
