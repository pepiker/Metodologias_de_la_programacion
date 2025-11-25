# Wile

"""
    El while es un circulo controlado/comando
    por condicion.

    La estructura basica de un wile es:

    wilw conditional:
        action


"""

# While infinito
"""
    Programa si el usuario ingresa un numero 
    entre el 25 y 50, entonces esta dentro del rango
    y salirme del while,
    de otro modo pedirle que ingrese otro numero.
"""
while True:
    try:
        number = int(input("ingresa el numero:"))

        if number > 25 and number <= 50:
            print("Estas en el rango, lo hiciste bien")
            break
        else:
            print("Esta fuera de el rango, ingresa otro numero.")

    except ValueError:
        print("se ha introducido una variable no valida")
