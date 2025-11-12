#tuples 

"""

    Las tuplas son listas de elementos que no 
    cambian de tamaño. las tuplas son inmutables.

    se utilizan los parentesis para definir una tupla ().

"""

rectangle_measurements = (200,50) #largo y ancho
print(rectangle_measurements[0])
print(rectangle_measurements[1])

for measure in rectangle_measurements:
    print(measure)

#print(dir(rectangle_measurements)) #built-in directory


# Regresando tantito las lista
cars = ["bmw", "porche", "mazda"]
print(cars)
cars[0] = "bmw"
cars[1] = "porche"
cars[2] = "mazda"
print(cars)

rectangle_measurements = (200,50) # (largo y ancho)
#rectangle_measurements[0] = 300 #Error: las tuplas son inmutables
#rectangle_measurements[1] = 100 #Error: las tuplas son inmutables
rectangle_measurements = (300,100,1 ) # reasignacion de la tupla

"""
    No podemos modificar una tupla directamente
    lo que si podemos hacer es cambiar la asignacion
    a una variabble que almacena una tupla.

"""