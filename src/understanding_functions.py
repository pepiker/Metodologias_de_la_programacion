### FUNCIONES
#Las funciones son como bloques de codigo para realizar
#una tarea en especifico

# Cuando quereos realizar una tarea que se ha definido
#en la funcion, tenemos que llamar el nombre de la 
#funcion que realiza la accion.

"""

    Sintaxis de una funcion 
    
    def nombre_funcion()
        acciones

    Ejemplo: vamos a definir una funcion que de un
    saludo a crhistofer
"""

def gretting_christopher():
    """
    Funcion para saludar a una persona 
    llamada christopher.
    """
    for i in range(0,5):
        print("Hello christopher")

gretting_christopher()


# Ejemplo de una funcion que genere el nombre completo
# de una persona y lo regrese
#parametros pocisionales

def create_full_name ( firs_name, middle_name, last_name=""):
     full_name = f"{firs_name} {middle_name} {last_name}".title()
     return full_name.title()
    
user_firs_name = input("dame tu primer nombre:")
user_middle_name = input("dame tu segundo nombre:")
user_last_name = input("dame tu last name:")

# argumentos posicionales
generated_fullname = create_full_name(
     user_firs_name.strip().lower(),
     user_middle_name.strip().lower(),
     user_last_name.strip().lower())
    
print(generated_fullname)

#argumentos llave
generated_fullname(
    middle_name = user_middle_name,
    firs_name = user_firs_name,
    last_name = user_last_name,
)

#args en funciones
#kwargs en funciones
# Manaejos de datos (.txt, csv,exel,works,pdf,json)
# args via consola (sys)
# cli en python- comand line interface
# testing - casos de prueba(borde, validos, invalidos)
