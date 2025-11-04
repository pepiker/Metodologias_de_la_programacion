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

print("\n")
print("Agregar elementos a una lista")
print(bicycles)
print("Metodo de la lista para agregar elementos: list_name.append(element)")
bicycles.append("ducatti")
print(bicycles)
