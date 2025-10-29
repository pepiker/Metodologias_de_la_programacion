"""

    Un string es una manera sencilla una serie 
    de caracteres. En python , todo lo que se encuentre 
    dentro de las comillas (' ') o dobles (" ")
    sera considerado un string.

    Ejemplo:
    "Esto es un string"
    'Esto es un string'

    'Le dije a un amigo "python es mi lenguaje favorito"'
    "El lenguaje 'python' lleva el nombre por Monty Python , no por ser la serpiente"

"""

name = "clase de programacion"
print(name)


#title
print(name.title())

print(name)

"""
Un metodo es una accion que python
puede realizar en un fragmento de datos
o sobre la variable.

    El punto . despues de una variable 
seguido del metodo title() dice que 
se tiene que ejecutar el metodo title()
de la variable name.

    Todos los metodos van seguidos del parentesis 
    por que en ocaciones neccesita informacion adicional
    para funcionar, la cual iria dentro de los parentesis.
    En esta ocacion, el metodo .title() no requiere informacion 
    adicional para funcionar.

"""

print("metodo upper:", name.upper())
print("metodo lower:", name.lower())


# Concatenacion de STRINGS

first_name = "charly"
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name)
print(full_name .title())