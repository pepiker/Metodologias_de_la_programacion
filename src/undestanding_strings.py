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


#Whitespaces

"""
Un writespace se refiere a cualquier caracter que 
no se imprime, es decir un espacio, tabulador y 
finales de linea. Los Writespace se utilizan 
comunmente para organizar las salidas de tal manera
que sea mas amigable de leer o ver para el usuario

Ejemplo:
 -tabulador: \t
 -salto de linea: \n

"""
print("writespace Tabulador")
print("Python")
print("\tpython")
print("\t\tpython")


print("Writespace Salto de linea")
print("language: \n\tpython\nc\n\tJavascript")


#Eliminacion de espacios en blanco
programmcion_languages = " python "
print(programmcion_languages)
print(programmcion_languages.rstrip())
print(programmcion_languages.lstrip())
print(programmcion_languages.strip())



#Syntax Error con String
message = 'una fortaleza de python es su comunidad'
print(message)
message = 'una fortaleza de " pytho " es su comunidad'

# f-strings

famous_person = "Taylor Swift"
message = f"{famous_person} una vez dijo me voy al oxxo en avion"
print(message)

print( f"{famous_person.upper()} una vez dijo me voy al oxxo en avion")

"""
   Elige una persona famosa (quien tu quieras)
   Elige una cita famosa de esta persona
   Iguala ambos strings a una variable

   1) realiza la concatenacion utilizando el signo de suma
   2)utiliza la concatenacion utilizando fstring

"""



name_famous = "Cristiano Ronaldo"
quote = "cristiano es mejor que messi"
famous_message = name_famous + " " + quote
print(name_famous+" "+quote) 

f_string_message_ = f"{name_famous}{quote}"
print(f_string_message_)
