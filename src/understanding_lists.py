#Lists

"""
    Las listas nos permiten almacenar la informacion 
    en algun lugar, la cantidad que tenga: ya sean
    pocos elementos o millones de elementos.

    
    Se recomienda nombrar una variable de tipo lista 
    en plural.

    En python los corchetes [] definen una lista, 
    sus elementos van separados por comas.

    Las listas son elementos mutables, es decir se puede modificar.

    Ejemplo:

"""

bicycles = ['trek', 'canondale', 'redline', 'specialized', 'griant']

print(bicycles)
print(bicycles[0].title())

# Los indices comienzan en 0 y terminan en n-1

print(bicycles[4].title())

# Accediendo al ultimo elemento
print(bicycles[-1].title()) #ultimo elemento
print(bicycles[-2].title())
print(bicycles[-5].title()) #primer elemento

# Utilizando valores de la lista.

message = "mi primer bicicleta fue una " + bicycles[4].upper() + "."
print(message)

message_f = f"mi primer bicicleta fue una {bicycles[4].title()} ."
print(message_f)

## Agregar elementos a una lista

"""
    #Listas A-105
    Agrega elementos a una lista 
        -append(): Agregar elementos a una lista.
"""

print("\n-- agregar elemntos a una lista metodo append()---"  )
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki" ]
motorcycles.append("ducatti")
print(motorcycles) # salida: ["honda", "yamaha", "suzuki", "ducatti" ]
"""
agregar elemntos a una lista en una pocision especifica
- insert(): agrega un elemnto en una pocision especifica de la lista
""" 
print("\n-- agregar elemntos a una lista metodo insert()---"  )
motorcycles = ["honda", "yamaha", "suzuki"] 
print(motorcycles) # salida: ["honda", "yamaha", "suzuki" ]
motorcycles.insert(1, "ducatti")
print(motorcycles) # salida: ["ducatti", "honda", "yamaha", "suzuki" ]

"""
eliminar elemntos de una lista
- del: elimina un elemnto de una lista en una pocision especifica
"""
print("\n-- eliminar elemntos de una lista metodo del---"  )
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki" ]
del motorcycles[0]
print(motorcycles) # salida: ["honda", "suzuki" ]

""" 
Eliminar elemntos de una lista y usar el valor eliminado
- pop(): elimina y devuelve el ultimo elemnto de una lista
""" 
print("\n-- eliminar elemntoos de una lista y usar el valor eliminado metodo pop()---"  )
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki" ]
last_motorcycle = motorcycles.pop(1)
print(motorcycles) # salida: ["honda", "yamaha" ]
print(f"la ultima motocicleta que compre fue una {last_motorcycle},")


"""
Eliminar un elemnto especifico de una lista por valor
- remove(): elimina un elemnto especifico de una lista por valor
"""
print("\n-- eliminar un elemnto especifico de una lista por valor metodo remove()---"  )
motorcycles = ["honda", "yamaha", "suzuki", "ducatti"]
print(motorcycles) # salida: ["honda", "yamaha", "suzuki", "ducatti" ]
motorcycles.remove("ducatti")
print(motorcycles) # salida: ["honda", "yamaha", "suzuki" ]
print("\n")
# Nota: Si se desea usar el valor eliminado, es recomendable usar pop() en lugar de remove() ya que remove() no devuelve el valor eliminado.
# Fin del archivo understanding_lists.py


""""
#Listas A-105
organiza una lista permanentemente
- sort(): organiza una lista permanentemente en orden alfabetico        

"""

print("\n-- organiza una lista permanentemente metodo sort()---"  )
cars = ["bmw", "audi", "toyota", "subaru"]          
print(cars) # salida: ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # salida: ['audi', 'bmw', 'subaru', 'toyota']




"""

    Ejemplo:
"""
students = ["hosue", "victor", "ana", "mike", "paulo", "gerardo"]
print(students)
desired_students = input("que estudiante deseas borrar de la lista?: ")
students.remove(desired_students.strip().lower())
print(students)
print("tu has eliminado:", desired_students)
students.reverse()
print(students)
print(len(students))


cars_1 = ["bmw", "toyota", "subaru", "chevy", "tesla"]
sorted(cars_1)
sorted_list = sorted(cars_1)
print("lista original", cars_1)
print("lista ordenada temporalmente", sorted_list)
