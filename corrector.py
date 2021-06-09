import os
import sys
import importlib

files = os.listdir('.')
module_file = [f.split('.')[0] for f in files if 'grupo03' in f][0]

grupo = importlib.import_module(module_file)

samples = [
    ('''SELECT c.first_name,
               c.last_name
        FROM customers AS c''', {'customers': ['first_name', 'last_name']}),
    ('''SELECT c.first_name,
               c.last_name
        FROM customers AS c
        WHERE c.id = 2''', {'customers': ['first_name', 'id', 'last_name']}),
    ('''SELECT DISTINCT c.first_name,
                        c.last_name,
                        phones_numbers.number
        FROM customers AS c
            LEFT JOIN phones_numbers ON
                c.id = phones_numbers.customer_id
        ''', {'customers': ['first_name', 'id', 'last_name'],
              'phones_numbers': ['customer_id', 'number']}),
    ('''SELECT V.NROFACTURA, V.MONTO
        FROM VENTAS V
        WHERE V.MARCA_PAGO_CONTADO IS NULL 
        AND V.NROFACTURA NOT IN (SELECT FA.NROFACTURA FROM FACTURAS_ADEUDADAS FA)''',
		{'VENTAS': ['MARCA_PAGO_CONTADO', 'MONTO', 'NROFACTURA'],'FACTURAS_ADEUDADAS': ['NROFACTURA']}),
    ('''SELECT A.nombre, A.cantidad, COUNT(A.patas) AS 'Cantidad'
        FROM Animales A INNER JOIN Felinos F ON A.codigo=F.codigo
        GROUP BY A.nombre, A.cantidad, F.codigo
        HAVING COUNT(A.patas)>2
        ORDER BY A.nombre DESC''',
        {'Animales': ['cantidad', 'codigo', 'nombre', 'patas'],'Felinos': ['codigo']}),
    ('''SELECT A.Nombre, MAX(A.Nota) AS 'Nota_Alta', Profesores.Materia
        FROM Alumnos A
        LEFT JOIN Profesores ON A.Codigo=Profesores.Codigo 
        INNER JOIN Universidad AS U ON A.Numero=U.Numero
        WHERE A.Apellido='Lopez' AND (Profesores.Nombre='Jorge' OR Profesores.Edad>=50)
        GROUP BY A.Nombre, Profesores.Materia, U.Carrera, Profesores.DNI
        HAVING MIN(A.Edad)<>20
        ORDER BY A.Direccion''',
        {'Alumnos': ['Apellido', 'Codigo', 'Direccion', 'Edad', 'Nombre', 'Nota', 'Numero'],
        'Profesores': ['Codigo', 'DNI', 'Edad', 'Materia', 'Nombre'],
        'Universidad': ['Carrera', 'Numero']})
    ]

for ix, sample in enumerate(samples):
    print('***** Resultados test parsing ejemplo {} *****'.format(ix+1))
    print(sample[0])
    print('-' * 3, ' Fin consulta ', '-' * 3)

    try:
        result = grupo.parse_select_statement(sample[0])

        if result != sample[1]:
            resultStr = 'incorrecto'
        else:
            resultStr = 'correcto'

        print('El resultado de la comprobación fue {} !'.format(resultStr))
        print('Resultado entregado: ', result)
        print('Resultado esperado: ', sample[1])

    except Exception as e:
        print('''Se produjo una excepción al intentar parsear el ejemplo y/o 
                 comprobar el resultado !''')
        print(e)
    print('')